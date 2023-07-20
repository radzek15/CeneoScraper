<div align="center">
  <a href="https://github.com/radzek15/CeneoScraper"></a>
  <h1 align="center">Ceneo scraper</h1>
  <p align="justify">Application to automate the process of extracting data from Ceneo.pl, a popular online shopping platform. I started this project during my studies and completed it a year later. During the development process, I added many features, including Flask, Docker, Docker Compose, Jinja templates, and Bootstrap. I also made numerous changes to the Python code, implementing object-oriented programming, by dividing the application into classes.</p>
</div>

## Features

| Feature            | Description                                                                                                                                                                                                     |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Web Application    | <p align="justify">CeneoScraper is a user-friendly web application powered by the Flask framework. It provides an intuitive interface for users to easily interact with the scraping functionalities.</p>       |
| Easy usage         | <p align="justify">The application is containerized with Docker, making it easy to deploy and manage in various environments.</p>                                                                               |
| Web Scraping       | <p align="justify">CeneoScraper utilizes the powerful Beautiful Soup library to scrape data from Ceneo.pl. It efficiently navigates through the website's HTML structure to extract the desired information.</p> |
| Dynamic Content    | <p align="justify">Jinja templates are used to render dynamic content in HTML pages, providing a seamless user experience.</p>                                                                                  |
| Data Visualization | <p align="justify">The app presents scraped data in an easy-to-read format using "chart.js" for charts and "datatables" for interactive tables.</p>                                                             |
| Data Export        | <p align="justify">CeneoScraper allows users to download the scraped opinions in JSON format using "jsonpickle."</p>                                                                                                                                                                                         |

## Usage:

<div align="justify">

 * Firstly clone the repo with this command:
    * `git clone https://github.com/radzek15/CeneoScraper`
 * Build and run the Docker container:
   * `docker-compose up --build
 * Access the application in your web browser at `http://localhost:5000`. 
 * Eventually run tests:
   * Pytest and selenium will be available soon.
<h4 align=center>Demo Usage<h4>

https://github.com/radzek15/CeneoScraper/assets/79796741/8d4b6d5f-46e5-4f2d-837f-2445b480ec1b

## Tech Stack
   * Python3
   * Flask
   * Jinja2
   * Docker
   * Chart.js
   * Datatables
   * JSON
   * Bootstrap5
   * pytest
   * Selenium

## License
CeneoScraper is licensed under the [MIT](https://github.com/radzek15/CeneoScraper/blob/master/LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.

</div>
