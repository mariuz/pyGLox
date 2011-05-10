uniform float time;

void main(void)
{
	gl_FrontColor = gl_Color;
	gl_TexCoord[0] = gl_MultiTexCoord0;
	
	vec4 vt = gl_Vertex;

	vt.x += sin(time*vt.z/32);
	vt.y += sin(time*vt.y/32);
	vt.z += cos(time*vt.x/32);
	
	gl_Position = gl_ModelViewProjectionMatrix * vt;
	//gl_Position = ftransform();	
}
