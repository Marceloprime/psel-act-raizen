<h1>
   PSEL API de Previsão do Tempo - Act Digital
   <img loading="lazy" src="https://media.licdn.com/dms/image/D4D0BAQHseijE5tG-Jg/company-logo_200_200/0/1684846118400/act_digital_logo?e=2147483647&v=beta&t=DhTPTS2MPBjdX_2DMTJP-WXS0aDhux2rma__KffLQDU" alt="Logo" height="40px">
</h1>

<img loading="lazy" src="https://s3-sa-east-1.amazonaws.com/raizen-prod/items-images/post-209-1570407169284-logo-raizen-rgb.png" alt="Logo"/>

<h2>Descrição</h2>
<h3>A api é composta de 4 endpoints:</h3>

<strong>Consulta livre do clima</strong>
<p>Onde você pode consulta de forma livre, porém sem historico</p>
<code>GET http://0.0.0.0:5000/free/:city</code>
<br/><br/>

<strong>Criação de conta</strong>
<p>Aqui você pode criar uma conta e consequentemente salvar suas consuktas em um  historico</p>
<code>POST http://0.0.0.0:5000/account</code>
<br/><br/>

<strong>Consulta da conta</strong>
<p>Aqui você pode consulta seu id</p>
<code>GET http://0.0.0.0:5000/account/user/:email</code>
<br/><br/>

<strong>Consulta do clima com conta</strong>
<p>Aqui você pode consulta a previsão do clima e cada consulta é salvar no banco</p>
<code>GET http://0.0.0.0:5000/weather/:city/:account_id</code>
<br/><br/>

<strong>Histórico de consultas</strong>
<p>Aqui você pode consulta seu historico através do seu account_id</p>
<code>GET http://0.0.0.0:5000/history/:account_id</code>
<br/><br/>

<h2>Stack Tecnológica</h2>
   <ul>
      <li>flask</li>
      <li>mongodb</li>
      <li>pytest</li>
   </ul>
   
<h2>Setup e Teste</h2>
<h3>Rode o comando:</h3>
<code>docker-compose up --build</code>
<p>Para usar o api.http no vscode, instale a extenção <code>humao.rest-client</code></p>