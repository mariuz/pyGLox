uniform vec3 lightPos;
uniform float time;

varying vec3 normal, lightDir;
varying vec3 vertex, vv;

void main(void)
{
	// normal in eye space
 	normal = normalize(gl_NormalMatrix*gl_Normal);
 	
 	// light direction in eye space
	lightDir = normalize(vec3(gl_ModelViewMatrix*(vec4(lightPos,1)-gl_Vertex)));
	
	vertex = gl_Vertex.xyz;
	vv = -vec3(gl_ModelViewMatrix*gl_Vertex);

	gl_FrontColor = gl_Color;
	gl_TexCoord[0] = gl_MultiTexCoord0;
	
	vec4 vt = gl_Vertex;
	if(vt.x > 0.2)
	{
		vt.z += cos(time*0.5) * 0.3;
	}
	else
	{
		vt.z -= sin(time*0.5) * 0.3;
	}
	
	if(vt.y > 1.2)
	{
		vt.x -= sin(time*0.8) * 0.3;
	}
	else
	{
		vt.x += cos(time*0.8) * 0.3;
	}
	
	if(vt.y > 2.0)
	{
		vt.x -= sin(time*0.8) * 0.3;
	}
	else
	{
		vt.x += cos(time*0.8) * 0.3;
	}


	
	gl_Position = gl_ModelViewProjectionMatrix * vt;
	//gl_Position = ftransform();	
}
