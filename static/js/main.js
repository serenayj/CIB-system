$(document).ready(function () {

	//for connecting to server
	window.share = {};
	share.ws = $.gracefulWebSocket("ws://127.0.0.1:1035/ws");
	share.send = function (message) {
		share.ws.send(message);
	}

	share.ws.onmessage = function (event) {
		var messageFromServer = event.data;
		
		var list_element = document.createElement('li');
		
		// alert("before process, the message is : " + messageFromServer);

		try{

			if($.parseJSON(messageFromServer).type == "chat")
			{
//				alert("about to chat: " + messageFromServer);
			var user_speak = $('#curr-user-name').attr("value");
				$("#chat_box_text").prepend("<li>"+user_speak+":"+ $.parseJSON(messageFromServer).text + "</li>");
			}
			else if ($.parseJSON(messageFromServer).type == "share")
			{
//				alert("about to share: " + messageFromServer);
				var popitems = '<img src='+ $.parseJSON(messageFromServer).url+"><p>"+$.parseJSON(messageFromServer).name+'</p>';
				$("#itemlist").prepend("<li>" + popitems + "</li>")
				//$("#itemlist").after(popitems);
			}
		}catch(err)
		{
//			alert("catch message neither share nor chat: " +messageFromServer);
			$("#chat_box_text").prepend(messageFromServer);
		}


	};

	$('#empty').click(function(){
		$("#query").val("");
	});


	$('#search').click(function(){

		//testing Gilt api
		var shopstyle = "https://api.gilt.com/v1/products?q="+$('#query').val()+"&apikey=c77cb5f8dd6a77744a2c62eb2c8093c6deb0eb01f79fdf5129179b96154bdaab";
		$.ajax({
			type :"get",
			url : shopstyle,
			dataType: "json",
			success: function(data){
			
				$('#productlist').html(''); // clear the div's html contents for each time the query is processed
				for(var i=0; i< data['products'].length; i++) {

					var pre_texts = '<div class=col-sm-6 col-md-3><div class=thumbnail><div class=caption>';

					var name_brand = data['products'][i]['brand']+data['products'][i]['name']+'<p>'+data['products'][i]['skus'][0]['sale_price']+'</p>';//works well

					for(var j=0; j< data['products'][i]['image_urls']['91x121'].length; j++){

						var image_url = '<p><img src='+data['products'][i]['image_urls']['91x121'][j]['url']+'></p>';	
						var pre_append_text = pre_texts+name_brand+image_url+'</div></div></div>';
					
					};

					/*var pre_append_text = '<div class=col-sm-6 col-md-3><div class=thumbnail><div class=caption>'
                    	+"<img src="+data['products'][i]['image']['sizes']['Best']['url']+" /> <p>"+data['products'][i]['brandedName']+data['products'][i]['priceLabel']+'</p></div></div></div></div>';*/
				
						
				//append the product's name into the div as list elements
						$('#catalog').append(pre_append_text);
						//alert("done");
						
					// 	$(function() {
					// 		var current_img = $(this).find('img').attr('src');
					// 		$("#catalog .caption").tooltip({
								
								
					// 			contents:'<img src='+current_img+'style:height = 300px width=400px/>',
								
					// 		})；
							// below is the problem statement, its scope needs to be strictly defined.
							$( "#catalog .caption" ).draggable({
									appendTo: "body",
									helper: "clone"
								});
							//});
					// });
					};
					},
		});
		});
		$(function() {
			//set item to be draggable
			$( "#catalog li" ).draggable({
				appendTo: "body",
				helper: "clone"	
			});

			//set item to be droppable
			$( "#cart ul" ).droppable({
				//activeClass: "ui-state-default",
				//hoverClass: "ui-state-hover",
				activeClass: "ui-state-hover",
				hoverClass: "ui-state-active",
				accept: ":not(.ui-sortable-helper)",
				drop: function( event, ui ) {
				
					//$(this).append("<button class='rating' name ='Rate'></button>");
					$(ui.draggable.clone()).append("<button class='rating'name ='Rate'>Rate</button>");
					var droppeditems = $(ui.draggable.clone()).html();

					/*var ratingbtn = "<button class='rating' name ='Rate'>Rate</button>";
					$(ratingbtn).appendTo(this);*/

					
					var myObj = new Object();

					myObj.name = $("<div>").html($.parseHTML(droppeditems)).find('p').html();
					myObj.url = $("<div>").html($.parseHTML(droppeditems)).find('img').attr('src');
					myObj.type = "share";
					//alert($('#curr-user-name').attr('value'));
					myObj.userid = $('#curr-user-name').attr('value');//$("#curr-user-id").html();

					var passingObj = JSON.stringify(myObj);

					saveRecord(passingObj); // save the object into database

					share.send(passingObj);

					ratingsShow(droppeditems);

					},
				}).sortable({
				  items: "li:not(.placeholder)",
				  sort: function(){
					// gets added unintentionally by droppable interacting with sortable
					// using connectWithSortable fixes this, but doesn't allow you to customize active/hoverClass options
					$( this ).removeClass( "ui-state-default" );
					
				  }
				});

				//drag items to the board and items will be fixed size
				function markImage($item){
					$item.fadeOut("slow",function(){
						$item.find(".placeholder").remove()
						.end()
						.css("width","80px")
						.appendTo(this)
						.find("img")
						.css("height","72px")
						.end()
						.clone()
						.appendTo('.placeholder')
						.fadeIn();
						//.append("<button class='rating' name ='Rate'></button>");
					});
				};



				function commentShow(){
					function handler(event){
						$('#comment').click(function(){
							//working on comment box, referenced from jsfiddle
							var commenttext = "<div id='msgbox'><p>Please enter any additional comments:</p><textarea id='ta' rows='5' cols='30'></textarea>"
							var target = $("#mytext").val();
							$('#itemcomment').html(commenttext);
							$('#msgbox').dialog({
								autoOpen:false,
								modal:true,
								title: 'Add Comments',
								buttons: {
									Okay: function() {
										var oldComments = $("#theDescription").html();
										var newComments = $('#ta').val();
										$('p.comment').html(oldComments +'<br />' + newComments);
										$(this).dialog('close');
									},
									Cancel: function() {
										$(this).dialog('close');
									}
								},
								close: function() {
									alert('AJAX update completed');
								}
							});
						$('#msgbox').dialog('open');
						});
                    }
				$('button').click(handler).find('button').hide();
			};

				function ratingsShow(item){
					alert("start rating!");
					/*<input id="input-6a" class="rating" data-size="xs">
                    <script>
                    $("#input-6a").on("rating.change", function(event, value, caption) {
                      $("#input-6a").rating("refresh", {disabled: true, showClear: false});
                    });
                    </script>*/
					var testhtml = "<input id='input-6a'class=rating'data-size='xs><script>$('#input-6a').on('rating.change',function(event, value,caption){$('#input-6a').rating(refresh',{disabled: true, showClear: false});});</script>";
					$(item).append(testhtml);
					alert("ratings over");
				};
		});
	});