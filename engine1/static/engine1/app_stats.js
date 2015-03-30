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
    
})();
