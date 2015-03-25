(function(){
    var app = angular.module("statsApp", []);

    app.controller('StatsController', function(){
        this.browsers = browsers;
        this.terms = terms;
    });

    app.controller('TabController', function(){
        /*Tab automatically starts with 1, which is Search Terms */
        this.tab=1;

        /*Method to set tab on user click*/
        this.setTab = function(tabToSet){
            this.tab = tabToSet;
        };

        /*Method to check if the current tab is set. Used to highlight the 
         * current tab. Returns True/False. */
        this.isTabSet = function(tabToCheck){
            return this.tab === tabToCheck;
        };
    });

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
