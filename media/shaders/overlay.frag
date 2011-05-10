uniform sampler2D texture;
uniform float time;

void main(void)
{	
	gl_FragColor = texture2D(texture, gl_TexCoord[0].st) * 0.8;
}
