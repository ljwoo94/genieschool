

//Gigagenie common JS

var apistatus=0;
var options={};
var ws;
var status='NI';
var appid;
var containerid;
var wsstate=0;
var initstate=0;
var authcode;

function init() {
	options={};
	options.apikey="RTUwMDQwMTl8R0JPWERFVk18MTU3ODQ0Mzk3OTM0MA=="; // api key given from developer portal
	options.keytype="GBOXDEVM"; // 개발자모드를 설정하고 사용하세요.
	
	gigagenie.init(options,function(result_cd,result_msg,extra){
	if(result_cd===200){
		status='IS';
		console.log('Initialize Success');
		alert("Page successfully Initialized");
		}
	});
};


function sendTTS(tts) {
	options={};
	options.ttstext = tts;
	gigagenie.voice.sendTTS(options, function(result_cd, result_msg, extra) {
		//	console.log("gigagenie.voice.sendTTS - result_cd:" + result_cd);
		//	console.log("gigagenie.voice.sendTTS - result_msg:" + result_msg);
		alert("result_cd :" + result_cd);
		alert("result_msg: " + result_msg);
	});
};

function ask() {
	var options={};
	options.voicemsg="애스크 샘플입니다. TTS가 아닙니다.";
	gigagenie.voice.getVoiceText(options, function(result_cd, result_msg, theme) {
			if(result_cd===200) {
				console.log(theme.voicetext);
				if(theme.voicetext.includes("예절")) {
					alert(theme.voicetext + "모드를 시작");
					location.href = "/polite_theme";
				}
				alert(theme.voicetext+"Mode");
			} else
				alert("result != 200");
		});
};
