(function(){
    var app = angular.module("statsApp", []);
    
    app.controller('StatsController', ['$http', function($http){
        /*Initialize variables as empty arrays so the initial load doesn't 
         * create errors.*/
        var stats = this;
        stats.browsers = [];
        stats.terms = [];

        /*Use $http.get() to fetch our JSON data for browsers.*/
        $http.get('stats_browsers').success(function(data){
            stats.browsers = data;
        });

        /*Use $http.get() to fetch our JSON data for search terms.*/
        $http.get('stats_terms').success(function(data){
            stats.terms = data;
        });

    }]);

    app.directive('statsTabs', function(){
        return {
            restrict: 'E',
            templateUrl: 'stats-tabs',
            controller: function(){
                this.tab = 1;
                this.setTab = function(tabToSet){
                    this.tab = tabToSet;
                };
                this.isTabSet = function(tabToCheck){
                    return this.tab === tabToCheck;
                };
            },
            controllerAs: 'tab'
        };
    });
    
    app.filter('searchFilter', function(){
        /*Filters must return a function. Here array is our array of all the 
         * search stats, and searchString is the user input.*/
        return function(array, searchString){
            /*If user did not enter string, return entire array*/
            if (!searchString){
                return array;
            }
            /*Otherwise we only want to return terms that include the user 
             * input.*/
            var resultArray = [];
            /*We want the search to be case insensitive.*/
            searchString = searchString.toLowerCase();
            /*Every term that includes the searchString gets added to our new
             * array, resultArray.*/
            angular.forEach(array, function(term){
                /*If the searchString is in term.name, add to resultArray*/
                termNameLowercase = term.name.toLowerCase();
                if(termNameLowercase.indexOf(searchString) !== -1){
                    resultArray.push(term);
                }
            });
            return resultArray;
        };
    });

})();
