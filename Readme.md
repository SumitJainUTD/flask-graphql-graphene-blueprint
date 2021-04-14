1. Clone the repo
2. run the app by 'python main.py'
3. Once app is running - make call from browser 'http://0.0.0.0:5001/graphql' this will create the database.
4. In separate terminal run 'sqlite3 db.sqlite3',  run all the queries from **_create_data.txt_** file.
5. Nom from 'http://0.0.0.0:5001/graphql', make a call with body 
````{
  conferences {
    name
    year
    conferenceTalks {
      title
      videoUrl
      speakers {
        firstName
      }
    }
     conferenceTags {
       tagName
     }
  }
}
````
You should output as below:
````{
  "data": {
    "conferences": [
      {
        "name": "conference_ference_one",
        "year": "2020",
        "conferenceTalks": [
          {
            "title": "con_talk_1",
            "videoUrl": "google.com",
            "speakers": [
              {
                "firstName": "sumit"
              }
            ]
          },
          {
            "title": "con_talk_2",
            "videoUrl": "aaa.com",
            "speakers": []
          },
          {
            "title": "con_talk_3",
            "videoUrl": "bbb.com",
            "speakers": []
          }
        ],
        "conferenceTags": [
          {
            "tagName": "python"
          },
          {
            "tagName": "js"
          },
          {
            "tagName": "java"
          }
        ]
      },
      {
        "name": "conference_ference_teo",
        "year": "2019",
        "conferenceTalks": [
          {
            "title": "con_talk_4",
            "videoUrl": "ccc.com",
            "speakers": [
              {
                "firstName": "ryan"
              }
            ]
          }
        ],
        "conferenceTags": [
          {
            "tagName": "java"
          }
        ]
      }
    ]
  }
}
````
