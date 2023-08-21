FROM mcr.microsoft.com/dotnet/sdk:7.0 as build-env
WORKDIR /App

COPY Program.cs dotnetcore.csproj  /App
RUN dotnet restore
RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/sdk:7.0
USER alper.cetin
WORKDIR /App
COPY --from=build-env /App/out .
ENTRYPOINT ["dotnet", "DotNet.Docker.dll"]
