## Week3
## Friday Cases
## Case 3
- # Case: Yagiz wanted us to build pipeline for java/maven app and do several stages.
- Step1: In order to maintain to run jvm I defined variables
- Step2: Build is doen on the maven:3.8 image.
- Step3: Test are done based on the maven cli opts
- Step4: Dockerized the app and pushed it onto the harbor account with insecure login
- Step5: Artifacts deployed according to the ci_settings.xml
- Step6: Static scanning done on the with the SonarQube

## Case 4
- # Case: Yagiz wanted us to build pipeline for .NET-Core app and do several stages.
- Step1: Object directory, nuget packages directory and source code path directory is defined.
- Step2: Build is doen on the dotnet:7.0 image.
- Step3: Test are done based on the dotnet test command
- Step4: Artifacts published packed and pushed to the package registry
- Step5: Dockerized the app and pushed it onto the harbor account with insecure login
- Step6: Static scanning done on the with the SonarQube