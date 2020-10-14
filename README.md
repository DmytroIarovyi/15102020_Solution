# Part 1

***Requirements:***
 - Python 3.5+
 - Chrome browser version 79+

***Used ENV:***
 - Linux 64 bit (16.04)
 - PyCharm IDE
 
***Used patterns and frameworks:***
 - Singleton
 - Page Factory Selenium
 - Selenium
 - Paho mqtt
 - pytest
 
***Packages to install:***
 - pip install selenium-page-factory
 - pip install paho-mqtt
 - go through files and add missed packages - they should be included in default python packages set
 

  Alternatively compare your packages with the ones below. Add manually if something is missed:

![alt text](https://github.com/DmytroIarovyi/Misc/blob/main/Screenshot%20from%202020-10-14%2015-23-43.png)




***Set 'Default test runner' - 'pytest':***

![alt text](https://github.com/DmytroIarovyi/Misc/blob/main/Screenshot%20from%202020-10-14%2015-20-33.png)


***Restrictions/Warnings***
 * <ins>...As long as tests are running on Lufthansa's PROD - next issues may/will occur:</ins>
 - Lufthansa may detect this is an automatic software
 - CAPTCHA test can be shown on any stage of browser navigation
 
 
   (to be able to run the test please put brakepoints in debug mode, pass CAPTCHA tests and then continue)



## Run app (tests)
*Entry point* - Run tests from here:  tests/search_flight/test_search_result.py

 
 
 # Part 2
 
 1. Verify data fomat correctness (dates, flight numbers, statuses, cities, timeformat, airlines etc.)
 2. Verify if it is sorted by date, time in a list. (or some other criteria depending on specs)
 3. Verify conflicting data, e.g. different airlines with the same flight number
 4. Verify statuses correctness (departed, arrived, in air) according to time now and departure, arrival times
 5. Verify each 10 seconds update is executed and new entries(y) appears in the list
 6. Verify new entries(y) appears on update requests (if there are any)
 7. Verify Search sorts out only data according to search request. (handle non-existent requests)
 8. Verify Filter sorts out data according to filter provided. Test with variety combinations
 9. Verify Alerts flow with invalid data (invalid email/phone number, offline device)
 10. Verify performance for : search, filter requests
 11. Verify error cases (connection, backend sends errors, etc) handling - (chaos monkeys can be used or simulation using api)
 12. Verify workability on other browsers, devices - desktop/mobile/tablet
 13. Verify Alerts workability (create alerts, ensure data is received as soon as it is available) - (you can compare the data available in a list with alert details)
 
