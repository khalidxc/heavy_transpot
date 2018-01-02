var data = [{
    title: 'All Day Event',
    start: '2015-02-01'
  },
  {
    title: 'Long Event',
    start: '2015-02-07',
    end: '2015-02-10'
  },
  {
    id: 999,
    title: 'Repeating Event',
    start: '2015-02-09T16:00:00'
  },
  {
    id: 999,
    title: 'Repeating Event',
    start: '2015-02-16T16:00:00'
  },
  {
    title: 'Conference',
    start: '2015-02-11',
    end: '2015-02-13'
  },
  {
    title: 'Meeting',
    start: '2015-02-12T10:30:00',
    end: '2015-02-12T12:30:00'
  },
  {
    title: 'Lunch',
    start: '2015-02-12T12:00:00'
  },
  {
    title: 'Meeting',
    start: '2015-02-12T14:30:00'
  },
  {
    title: 'Happy Hour',
    start: '2015-02-12T17:30:00'
  },
  {
    title: 'Dinner',
    start: '2015-02-12T20:00:00'
  },
  {
    title: 'Birthday Party',
    start: '2015-02-13T07:00:00'
  },
  {
    title: 'Click for Google',
    url: 'https://google.com/',
    start: '2015-02-28'
  }
];

var newData = [{
    title: 'stuff',
    start: '2015-03-01'
  },
  {
    title: 'stuff',
    start: '2015-03-02'
  }
];

$(document).ready(function() {
  $('#calendar').fullCalendar({
    customButtons: {
      AddEvent: {
        text: 'Add Event',
        click: function() {
          $('.fc-view-container').hide();
          $('#StudentList').hide();
          $('#AddEventForm').hide();
          $('#AddGeneralEvent').show();
        }
      },
      StudentList: {
        text: 'Student List',
        click: function() {
          $('.fc-view-container').hide();
          $('#AddEventForm').hide();
          $('#AddGeneralEvent').hide();
          $('#StudentList').show();
        }
      },
      ChooseCC: {
        text: 'Choose Course/Section',
        click: function() {
          $('#myModal').css("display", "block");
        }
      },
    },
    header: {
      left: 'prev,next today',
      center: 'title',
      right: 'ChooseCC, AddEvent ,StudentList ,month,agendaWeek,agendaDay'
    },
    defaultDate: '2015-02-12',
    editable: true,
    eventLimit: true, // allow "more" link when too many events
    events: data
  });

  $('.fc-center').click(function() {
    $('.fc-view-container').show();
  });
	$('.fc-center').css('cursor', 'pointer');

  $('#buttonGeneral1').click(function() {
    $('#AddEventForm').hide();
    $('#AddGeneralEvent').show();
  });

  $('#buttonPersonal1').click(function() {
    $('#AddGeneralEvent').hide();
    $('#AddEventForm').show();
  });

  $('#buttonGeneral2').click(function() {
    $('#AddEventForm').hide();
    $('#AddGeneralEvent').show();
  });

  $('#buttonPersonal2').click(function() {
    $('#AddGeneralEvent').hide();
    $('#AddEventForm').show();
  });


  $('#calendar').on('click', '.fc-next-button', function() {
    //alert('clicked');
    $('#calendar').fullCalendar('removeEvents');
    $('#calendar').fullCalendar('addEventSource', newData);
  });
  $('#calendar').on('click', '.fc-prev-button', function() {
    //alert('clicked');
    $('#calendar').fullCalendar('removeEvents');
    $('#calendar').fullCalendar('addEventSource', data);
  });

  var date = moment(new Date()); //today

  //more date options for your starting date:
  moment(date).format('MM-DD-YYYY');
  //var date = moment( "1-31-2017" );
  //var date = moment.unix(1485842400);  //unix date 1-31-2017
  //php to generate utc unix timestamp -> <? echo strtotime('2017-01-31')?>

  var format = "ddd M-D";

  var a = date.clone().format(format)
  $('.a').val(a);

  var b = date.clone().add(1, 'day').format(format);
  $('.b').val(b);

  var c = date.clone().startOf('isoWeek').subtract(1, 'day');
  $('.c').val(c);

  var dayindex = date.isoWeekday();
  var insWeekdays = $('.weekdays').find('ins');

  for (i = 0; i < 7; i++) {
    var idate = c.clone().add(i, 'day').format(format);
    insWeekdays.eq(i).text(idate);
    insWeekdays.eq(dayindex).closest('td').addClass('isToday');
  }

  $("span").click(function() {
    $('.modal').hide();
  });

  $("#applyCS").click(function() {
    $('.modal').hide();
  });

  // 	$(document).click(function(event) {
  //     if(!$(event.target).closest('#myModal').length) {
  //         if($('#myModal').is(":visible")) {
  //             $('#myModal').hide();
  //         }
  //     }
  // });


});
