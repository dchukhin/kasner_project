(function(){
    var app = angular.module("statsApp", []);
    console.log('aaa');

    app.controller('StatsController', function(){
        console.log('got here');
        this.browsers = browsers;
        this.terms = terms;
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
