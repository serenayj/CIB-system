 $(document).ready(function () {
 $('#submit').click(function(event){
        event.preventDefault();

        //  Declare SQL Query for SQLite
 
        //var createStatement = "CREATE TABLE IF NOT EXISTS User (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, useremail TEXT)";

        var selectAllStatement = "SELECT * FROM sampleapp_user";

        var insertStatement = "INSERT INTO sampleapp_user (username, userid, password, email) VALUES (?, ?,?,?)";

        //var updateStatement = "UPDATE User SET username = ?, useremail = ? WHERE id=?";

        var deleteStatement = "DELETE FROM sampleapp_user WHERE id=?";

        //var dropStatement = "DROP TABLE User";
        
        var userid = $("#userid").val();
        var username = $('#username').val();
        var password = $("#password").val();
        var email = $("#email").val();

        $.ajax({
            type:"POST",
            $(this).attr("href", "index.html");
            url:login_view,
            data :$("#form2").serialize();                                                                                                                                                      
       });



var db = openDatabase("cib", "1.0","cib Database", 200000);  // Open SQLite Database openDatabase(shortName, version, displayName, maxSize);

var dataset;

var DataType;

function insertRecord() // Get value from Input and insert record . Function Call when Save/Submit Button Click..

{

    db.transaction(function (tx) { tx.executeSql(insertStatement, [userid,username,password,email], loadAndReset, onError); });

    alert("records created!");

        //tx.executeSql(SQL Query Statement,[ Parameters ] , Sucess Result Handler Function, Error Result Handler Function );

    }

    function loadAndReset() //Function for Load and Reset...

{

    resetForm();

    showRecords()

}

function onError(tx, error) // Function for Hendeling Error...
 
{
 
    alert(error.message);
 
}


function showRecords() // Function For Retrive data from Database Display records as list

{

    $("#results").html('')

    db.transaction(function (tx) {

        tx.executeSql(selectAllStatement, [], function (tx, result) {

            dataset = result.rows;

            for (var i = 0, item = null; i < dataset.length; i++) {

                item = dataset.item(i);

                var linkeditdelete = '<li>' + item['username'] + ' , ' + item['useremail'] + '    ' + '<a href="#" onclick="loadRecord(' + i + ');">edit</a>' + '    ' +

                '<a href="#" onclick="deleteRecord(' + item['id'] + ');">delete</a></li>';

                $("#results").append(linkeditdelete);
                console.log(results.rows);

            }

        });

    });

}

 

})
});
