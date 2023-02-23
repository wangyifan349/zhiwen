<button onclick="sendFingerprint()">Send Fingerprint</button>
<script>
function sendFingerprint() {
  // 获取用户指纹信息
  const fingerprint = getFingerprint();
  
  // 创建XMLHttpRequest对象
  const xhr = new XMLHttpRequest();
  
  // 设置请求方法和URL
  xhr.open('POST', '/fingerprint', true);
  
  // 设置请求头
  xhr.setRequestHeader('Content-Type', 'application/json');
  
  // 发送POST请求
  xhr.send(JSON.stringify({ fingerprint: fingerprint }));
}
</script>
