// Global in-memory cache variable (clears on runtime recycle)
let networkDataCache = [
  { "name": "Kusum_PassView_Demo", "password": "API_Online_Waiting_For_Sync" }
];

export async function onRequest(context) {
  const { request } = context;
  const url = new URL(request.url);

  // Handle CORS Preflight Pre-checks
  if (request.method === "OPTIONS") {
    return new Response(null, {
      status: 204,
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization"
      }
    });
  }

  // GET Request: Serve data to the HTML Front-end UI Dashboard
  if (request.method === "GET") {
    return new Response(JSON.stringify(networkDataCache), {
      status: 200,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
        "X-Powered-By": "Kusum PassView API v2"
      }
    });
  }

  // POST Request: Securely receive records transmitted from your local machine
  if (request.method === "POST") {
    try {
      const payload = await request.json();
      
      if (!Array.isArray(payload)) {
        return new Response(JSON.stringify({ error: "Payload must be an array" }), { 
          status: 400, 
          headers: { "Content-Type": "application/json" } 
        });
      }

      // Update the active cluster storage memory mapping
      networkDataCache = payload;

      return new Response(JSON.stringify({ status: "success", count: payload.length }), {
        status: 200,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" }
      });
    } catch (e) {
      return new Response(JSON.stringify({ error: "Invalid JSON structure payload" }), { 
        status: 400, 
        headers: { "Content-Type": "application/json" } 
      });
    }
  }

  return new Response("Method not allowed", { status: 405 });
}
