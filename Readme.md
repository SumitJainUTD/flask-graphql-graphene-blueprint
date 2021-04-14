1. Clone the repo
2. run the app by 'python main.py'
3. Once app is running - make call from browser 'http://0.0.0.0:5001/graphql' this will create the database.
4. In separate terminal run 'sqlite3 db.sqlite3',  run all the queries from **_create_data.txt_** file.
5. Nom from 'http://0.0.0.0:5001/graphql', make a call with body 
````{
  companies {
    name
    industry
    employees{
      title
      project
      profile {
        firstName
      }
      skills{
        skillName
      }
    }
  }
}
````
You should output as below:
````{
  "data": {
    "companies": [
      {
        "name": "Lucid LLC",
        "industry": "IT",
        "employees": [
          {
            "title": "SDE",
            "project": "Core",
            "profile": [
              {
                "firstName": "Sumit"
              }
            ],
            "skills": [
              {
                "skillName": "Java"
              }
            ]
          },
          {
            "title": "SDET",
            "project": "Core",
            "profile": [
              {
                "firstName": "Ryan"
              }
            ],
            "skills": [
              {
                "skillName": "Java"
              },
              {
                "skillName": "Python"
              }
            ]
          },
          {
            "title": "SDET",
            "project": "Platform",
            "profile": [
              {
                "firstName": "Jhon"
              }
            ],
            "skills": [
              {
                "skillName": "Python"
              }
            ]
          }
        ]
      },
      {
        "name": "Intel",
        "industry": "Hardware",
        "employees": [
          {
            "title": "SE",
            "project": "Engine",
            "profile": [
              {
                "firstName": "Carl"
              }
            ],
            "skills": [
              {
                "skillName": "JS"
              }
            ]
          }
        ]
      }
    ]
  }
}
````
