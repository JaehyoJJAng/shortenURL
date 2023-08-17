# ShortenURL

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)


이 프로젝트는 python과 fastapi를 이용해서 유저에게 url을 입력받아 해당 url을 축약해주는 프로젝트입니다.

<br>

# On Docker

**도커 환경에서 사용 시 아래 가이드를 읽고 따라해주세요**

## 1. install project
    `git clone https://github.com/JaehyoJJAng/shortenURL.git`

## 2. run app
    `docker-compose up -d --build`

<br>

# On Local

**로컬 환경에서 사용 시 아래 가이드를 읽고 따라해주세요.**

## install project
    `git clone https://github.com/JaehyoJJAng/shortenURL.git`

### install dependency
    `docker-compose up -d --build `

## run app
    uvicorn main:app --reload