pipeline
{
    agent
    {
        label 'linux'
    }
    stages
    {
        stage('Checkout')
        {
            steps
            {
                checkout scm
            }
        }
        stage("Check Environment")
        {
            steps
            {
                sh 'python3 --version'
                sh 'python3 -m pip --version'
            }
        }
        stage("Install Dependencies")
        {
            steps
            {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/python -m pip install --upgrade pip'
                sh '.venv/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Run Tests')
        {
            steps
            {
                sh '.venv/bin/python -m pytest -v -n 2 --html=reports/jenkins_test_report.html --self-contained-html --junitxml=reports/jenkins_junit_report.xml'
            }
        }
    }
    post
    {
        always
        {
            junit 'reports/jenkins_junit_report.xml'
            archiveArtifacts artifacts: 'reports/jenkins_test_report.html',
                         allowEmptyArchive: true
        }
    }
}