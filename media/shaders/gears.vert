uniform vec3 lightPos;
uniform float time;
uniform float beat;

varying vec3 normal, lightDir;
varying vec3 vertex, vv, nnn, tp;

void main(void)
{
	// normal in eye space
 	normal = normalize(gl_NormalMatrix*gl_Normal);
 	nnn = gl_Normal;
 	
 	// light direction in eye space
	lightDir = normalize(vec3(gl_ModelViewMatrix*(vec4(lightPos,1)-gl_Vertex)));
	
	vertex = gl_Vertex.xyz;
	vv = -vec3(gl_ModelViewMatrix*gl_Vertex);

	gl_FrontColor = gl_Color;
	gl_TexCoord[0] = gl_MultiTexCoord0;
	
	vec4 vt = gl_Vertex;

	//vt.x = vt.x*cos(beat) - vt.z*sin(beat);
	//vt.z = vt.x*sin(beat) + vt.z*cos(beat);
	//vt.y = vt.y * 2;
	
	/*mat2 rotY = mat2(cos(beat), 
				    -sin(beat), 
				     sin(beat), 
				     cos(beat));*/
				     
	//vt.xz = vt.xz * rot;

	
	//vt.x += cos(time) * beat;
	//vt.z += sin(time) * beat;
	
	//vt.y = cos(time) * vt.y;
	//vt.z = sin(time) * vt.z;
	
	//gl_Position = gl_ModelViewProjectionMatrix * vt;
	gl_Position = ftransform();	
	tp = gl_Position.xyz;
}
