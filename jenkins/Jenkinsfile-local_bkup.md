pipeline {
    agent any

    environment {
        PROJECT_DIR = "/workspace/mlflow-homePrice"
        IMAGE_NAME = "house-price"
        IMAGE_TAG = "v1"
        CONTAINER_NAME = "house-api"
    }

    stages {
        stage('Verify Project') {
            steps {
                dir("${PROJECT_DIR}") {
                    sh '''
                    pwd
                    ls -la
                    '''
                }
            }
        }
        
        stage('Debug') {
        steps {
        sh '''
        whoami
        pwd
        echo $PATH

        which python3 || true
        python3 --version || true

        which pip3 || true
        pip3 --version || true

        python3 -m pip --version || true
        '''
    }
}

       stage('Install Dependencies') {
      steps {
        dir("${PROJECT_DIR}") {
            sh '''
            python3 -m venv venv
            . venv/bin/activate
            python -m pip install --upgrade pip
            pip install -r requirements.txt
            '''
        }
    }
}

        stage('Train Model') {
            steps {
                dir("${PROJECT_DIR}") {
                    sh '''
                    python3 train.py
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${PROJECT_DIR}") {
                    sh '''
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker rm -f ${CONTAINER_NAME} || true

                docker run -d \
                  --name ${CONTAINER_NAME} \
                  -p 8080:1234 \
                  ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }
    }
}
