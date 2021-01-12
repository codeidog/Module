pipeline{
    agent any
    stages{
        stage("Build"){
            steps{
                echo "========executing Build========"
                //Set the version
                sh 'echo "VERSION=$BUILD_NUMBER" > .env'
                sh 'cat .env'
                //Build the application
                sh 'docker-compose build module'
            }
            post{                
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
        stage("Test"){
            steps{
                echo "========executing Test========"
                sh 'docker build -f Test/Dockerfile -t test-image .'
            }
            post{                
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }

        stage("Deploy"){
            steps{
                echo "========executing Test========"
                sh 'docker-compose up -d'
            }
            post{                
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }
    post{        
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}