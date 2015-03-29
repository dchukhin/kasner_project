(function(){
    var app = angular.module("statsApp", []);

    app.controller('StatsController', function(){
        this.browsers = browsers;
        this.terms = terms;
    });
    
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
/* 
    app.controller('TabController', function(){
        this.tab=1;

        this.setTab = function(tabToSet){
            this.tab = tabToSet;
        };

        this.isTabSet = function(tabToCheck){
            return this.tab === tabToCheck;
        };
    });
*/
    var browsers = [
        {"name":"firefox", "count": 20},
        {"name":"chrome", "count": 10}
    ];

    var terms = [
        {"name":"yahoo", "count":2},
        {"name":"google", "count":10},
        {"name":"ESPN","count":3}
    ];
/*

        {"browsers":[
            {"name":"firefox"},
            {"name":"chrome"}
            ]
        },
        {"terms":[
            {"name":"google"},
            {"name":"yahoo"},
            {"name":"ESPN"}
            ]
        }       
        ]
*/
})();
