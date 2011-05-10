uniform vec3 lightPos;
uniform float time;

varying vec3 normal, lightDir, lightSpotDir;
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
//	float tmp = vt.z;
//	vt.z = vt.y;
//	vt.y = tmp;
	
/*	if(vt.z < 0)
		vt.z -= sin(time*0.1*15) + 1;
	else if(vt.z > 0)
		vt.z += sin(time*0.1*15) + 1; */

	if(vt.z < -5)
		vt.z -= sin(time*0.1*15) + 1;
	else if(vt.z > 5)
		vt.z += sin(time*0.1*15) + 1;

	
	//gl_Position = gl_ModelViewProjectionMatrix * vt;
	gl_Position = ftransform();	
}
