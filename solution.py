class Information:
    """The class described information about schedule."""
    faculty = []
    bi = []
    cyb = []
    man = []
    soc = []
    jur = []

    @classmethod
    def write(cls, file_name):
        """Class method for write file."""
        cls.file_name = file_name
        with open(cls.file_name) as file:
            lines = file.readlines()
            Information.bi = lines[2:8]
            Information.cyb = lines[9:15]
            Information.man = lines[16:22]
            Information.soc = lines[23:29]
            Information.jur = lines[30:36]


class Business_Informatics(Information):
    """The class describes the schedule students in Business-Informatics."""

    __faculty = 'Economic faculty,Business-Informatics,Cybernetics,Management,Sociology,Jurisprudence'

    def __init__(self):
        """Initialization method."""

        self.bi = Information.bi
        self.monday_bi = self.bi[0].split(',')
        self.tuesday_bi = self.bi[1].split(',')
        self.wednesday_bi = self.bi[2].split(',')
        self.thursday_bi = self.bi[3].split(',')
        self.friday_bi = self.bi[4].split(',')
        self.saturday_bi = self.bi[5].split(',')

    def __str__(self):
        """String output method."""

        Business_Informatics.__faculty = Business_Informatics.__faculty.split(',')

        result = ''
        result += '*************************************************************************************' \
                  '***************************************************************' + '\n'
        result += f'*                                                    SCHEDULE STUDENTS OF ' \
                  f'{Business_Informatics.__faculty[0].upper()}                                           ' \
                  f'              *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'
        result += f'*                                                           ' \
                  f' {Business_Informatics.__faculty[1].upper()}                                               ' \
                  f'                            *' + '\n'
        result += '***************************************************************************************' \
                  '*************************************************************' + '\n'
        result += f'*         {self.monday_bi[0].upper()}        *        {self.tuesday_bi[0].upper()}       ' \
                  f' *        {self.wednesday_bi[0].upper()}        *        {self.thursday_bi[0].upper()}    ' \
                  f'    *        {self.friday_bi[0].upper()}        *        {self.saturday_bi[0].upper()}    ' \
                  f'    *' + \
                  '\n'
        result += '********************************************************************************************' \
                  '********************************************************' + '\n'
        result += f'*   {self.monday_bi[1]}  * {self.tuesday_bi[1]} *        {self.wednesday_bi[1]}          *' \
                  f'     {self.thursday_bi[1]}     *        {self.friday_bi[1]}       *     {self.saturday_bi[1]} ' \
                  f'    *' + '\n'

        result += f'*           {self.monday_bi[2][:-1]}          * {self.tuesday_bi[2]}       *      ' \
                  f'  {self.wednesday_bi[2]}      *  {self.thursday_bi[2]} *   {self.friday_bi[2]} *    ' \
                  f' {self.saturday_bi[2]}     *' + '\n'
        result += f'*           -           * {self.tuesday_bi[3][:-1]} *        {self.wednesday_bi[3]}   *    ' \
                  f'       {self.thursday_bi[3][:-1]}           * {self.friday_bi[3][:-1]}*    ' \
                  f'  {self.saturday_bi[3][:-1]}       *' + '\n'
        result += f'*           -           *           -           *   {self.wednesday_bi[4][:-1]}   *   ' \
                  f'         -           * {self.friday_bi[3][:-1]}*            -           *' + '\n'
        result += '*******************************************************************************************' \
                  '*********************************************************' + '\n'

        return result

    def __repr__(self):
        """Output method."""

        return self.__str__()


class Cybernetics:
    """The class describes the schedule students in Cybernetics."""

    __faculty = 'Economic faculty,Business-Informatics,Cybernetics,Management,Sociology,Jurisprudence'

    def __init__(self):
        """Initialization method."""

        self.cyb = Information.cyb
        self.monday_cyb = self.cyb[0].split(',')
        self.tuesday_cyb = self.cyb[1].split(',')
        self.wednesday_cyb = self.cyb[2].split(',')
        self.thursday_cyb = self.cyb[3].split(',')
        self.friday_cyb = self.cyb[4].split(',')
        self.saturday_cyb = self.cyb[5].split(',')

    def __str__(self):
        """String output method."""

        Cybernetics.__faculty = Cybernetics.__faculty.split(',')

        result = ''
        result += '*************************************************************************************' \
                  '***************************************************************' + '\n'
        result += f'*                                                    SCHEDULE STUDENTS OF ' \
                  f'{Cybernetics.__faculty[0].upper()}                                           ' \
                  f'              *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'
        result += f'*                                                           ' \
                  f' {Cybernetics.__faculty[2].upper()}                                               ' \
                  f'                            *' + '\n'
        result += '***************************************************************************************' \
                  '*************************************************************' + '\n'
        result += f'*         {self.monday_cyb[0].upper()}        *        {self.tuesday_cyb[0].upper()}  ' \
                  f'      *        {self.wednesday_cyb[0].upper()}        *        {self.thursday_cyb[0].upper()} ' \
                  f'       *        {self.friday_cyb[0].upper()}        *        {self.saturday_cyb[0].upper()}      ' \
                  f'  *' + \
                  '\n'
        result += '*****************************************************************************************' \
                  '***********************************************************' + '\n'

        result += f'*      {self.monday_cyb[1]}       * {self.tuesday_cyb[1]} *   {self.wednesday_cyb[1]} ' \
                  f'   *     {self.thursday_cyb[1]}     *  {self.friday_cyb[1]}  *     {self.saturday_cyb[1]} ' \
                  f'    *' + '\n'
        result += f'*      {self.monday_cyb[2]}       *       {self.tuesday_cyb[2]}         * ' \
                  f' {self.wednesday_cyb[2]}  *  {self.thursday_cyb[2]} *        {self.friday_cyb[2]}     ' \
                  f'  *     {self.saturday_cyb[2][:-1]}     *' + '\n'
        result += f'*          {self.monday_cyb[3]}           * {self.tuesday_cyb[3][:-1]}    *      ' \
                  f'{self.wednesday_cyb[3][:-1]}         *          {self.thursday_cyb[3]}            *     ' \
                  f'   {self.friday_cyb[3][:-1]}    *            -           *' + '\n'
        result += f'*       {self.monday_cyb[4][:-1]}          *           -           *            -       ' \
                  f'     *          {self.thursday_cyb[4][:-1]}        *           -          *            -     ' \
                  f'      *' + '\n'
        result += '*******************************************************************************************' \
                  '*********************************************************' + '\n'

        return result

    def __repr__(self):
        return self.__str__()


class Management:
    """The class describes the schedule students in Cybernetics."""

    __faculty = 'Economic faculty,Business-Informatics,Cybernetics,Management,Sociology,Jurisprudence'

    def __init__(self):
        """Initialization method."""

        self.man = Information.man
        self.monday_man = self.man[0].split(',')
        self.tuesday_man = self.man[1].split(',')
        self.wednesday_man = self.man[2].split(',')
        self.thursday_man = self.man[3].split(',')
        self.friday_man = self.man[4].split(',')
        self.saturday_man = self.man[5].split(',')

    def __str__(self):
        """String output method."""

        Management.__faculty = Management.__faculty.split(',')

        result = ''
        result += '*************************************************************************************' \
                  '***************************************************************' + '\n'
        result += f'*                                                    SCHEDULE STUDENTS OF ' \
                  f'{Management.__faculty[0].upper()}                                           ' \
                  f'              *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'
        result += f'*                                                            ' \
                  f'{Management.__faculty[3].upper()}                                                ' \
                  f'                            *' + '\n'
        result += '*****************************************************************************************' \
                  '***********************************************************' + '\n'
        result += f'*         {self.monday_man[0].upper()}        *        {self.tuesday_man[0].upper()}      ' \
                  f'  *        {self.wednesday_man[0].upper()}        *        {self.thursday_man[0].upper()}   ' \
                  f'     *        {self.friday_man[0].upper()}        *        {self.saturday_man[0].upper()[:-1]}' \
                  f'      ' \
                  f'  *' + \
                  '\n'
        result += '*****************************************************************************************' \
                  '***********************************************************' + '\n'

        result += f'*        {self.monday_man[1]}        *   {self.tuesday_man[1]}     *  ' \
                  f'  {self.wednesday_man[1]}       *        {self.thursday_man[1]}         *      ' \
                  f' {self.friday_man[1]}     *            -           *' + '\n'
        result += f'*  {self.monday_man[2]}   *  {self.tuesday_man[2]}   *{self.wednesday_man[2]}*        ' \
                  f'  {self.thursday_man[2]}            *{self.friday_man[2]}*            -           *' + '\n'
        result += f'*          {self.monday_man[3]}           *     {self.tuesday_man[3][:-1]}     * ' \
                  f' {self.wednesday_man[3][:-1]}     *   {self.thursday_man[3][:-1]}   *     ' \
                  f'  {self.friday_man[3]}     *            -           *' + '\n'
        result += f'*  {self.monday_man[4]}   *        {self.tuesday_man[4][:-1]}          *          ' \
                  f'  -            *            -           * {self.friday_man[4][:-1]}  *            - ' \
                  f'          *' + '\n'
        result += f'*  {self.monday_man[5][:-1]}   *           -           *            -            *     ' \
                  f'       -           *           -          *            -           *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'

        return result

    def __repr__(self):
        """Output method."""

        return self.__str__()


class Sociology:
    """The class describes the schedule students in Sociology."""

    __faculty = 'Economic faculty,Business-Informatics,Cybernetics,Management,Sociology,Jurisprudence'

    def __init__(self):
        """Initialization method."""

        self.soc = Information.soc
        self.monday_soc = self.soc[0].split(',')
        self.tuesday_soc = self.soc[1].split(',')
        self.wednesday_soc = self.soc[2].split(',')
        self.thursday_soc = self.soc[3].split(',')
        self.friday_soc = self.soc[4].split(',')
        self.saturday_soc = self.soc[5].split(',')

    def __str__(self):
        """String output method."""

        Sociology.__faculty = Sociology.__faculty.split(',')

        result = ''
        result += '*************************************************************************************' \
                  '***************************************************************' + '\n'
        result += f'*                                                    SCHEDULE STUDENTS OF ' \
                  f'{Sociology.__faculty[0].upper()}                                           ' \
                  f'              *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'
        result += f'*                                                           ' \
                  f' {Sociology.__faculty[4].upper()}                                           ' \
                  f'                                  *' + '\n'
        result += '*************************************************************************************' \
                  '***************************************************************' + '\n'
        result += f'*         {self.monday_soc[0].upper()}        *        {self.tuesday_soc[0].upper()}     ' \
                  f'   *        {self.wednesday_soc[0].upper()}        *        {self.thursday_soc[0].upper()} ' \
                  f'       *        {self.friday_soc[0].upper()}        *        {self.saturday_soc[0].upper()} ' \
                  f'       *' + \
                  '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'

        result += f'* {self.monday_soc[1]}  *        {self.tuesday_soc[1]}        *     {self.wednesday_soc[1]}' \
                  f'      *   {self.thursday_soc[1]}   *  {self.friday_soc[1]}   *   {self.saturday_soc[1][:-1]}' \
                  f'    *' + '\n'
        result += f'* {self.monday_soc[2]}    *   {self.tuesday_soc[2]}     *          {self.wednesday_soc[2]}' \
                  f'          *           {self.thursday_soc[2]}           *        {self.friday_soc[2]}    ' \
                  f'   *            -           *' + '\n'
        result += f'*          {self.monday_soc[3][:-1]}           * {self.tuesday_soc[3]}    * ' \
                  f' {self.wednesday_soc[3]}     *   {self.thursday_soc[3][:-1]}   *   {self.friday_soc[3]}  ' \
                  f'   *            -           *' + '\n'
        result += f'*           -           *          {self.tuesday_soc[4][:-1]}          *  ' \
                  f' {self.wednesday_soc[4][:-1]}   *            -           *   {self.friday_soc[4][:-1]} ' \
                  f'   *            -           *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'

        return result

    def __repr__(self):
        """Output method."""

        return self.__str__()


class Jurisprudence:
    """The class describes the schedule students in Cybernetics."""

    __faculty = 'Economic faculty,Business-Informatics,Cybernetics,Management,Sociology,Jurisprudence'

    def __init__(self):
        """Initialization method."""

        self.jur = Information.jur
        self.monday_jur = self.jur[0].split(',')
        self.tuesday_jur = self.jur[1].split(',')
        self.wednesday_jur = self.jur[2].split(',')
        self.thursday_jur = self.jur[3].split(',')
        self.friday_jur = self.jur[4].split(',')
        self.saturday_jur = self.jur[5].split(',')

    def __str__(self):
        """String output method."""

        Jurisprudence.__faculty = Jurisprudence.__faculty.split(',')

        result = ''
        result += '*************************************************************************************' \
                  '***************************************************************' + '\n'
        result += f'*                                                    SCHEDULE STUDENTS OF ' \
                  f'{Jurisprudence.__faculty[0].upper()}                                           ' \
                  f'              *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'
        result += f'*                                                          ' \
                  f'  {Jurisprudence.__faculty[5].upper()}                                                ' \
                  f'                         *' + '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'
        result += f'*         {self.monday_jur[0].upper()}        *        {self.tuesday_jur[0].upper()}      ' \
                  f'  *        {self.wednesday_jur[0].upper()}        *        {self.thursday_jur[0].upper()}' \
                  f'        *        {self.friday_jur[0].upper()}        *        {self.saturday_jur[0].upper()}' \
                  f'        *' + \
                  '\n'
        result += '****************************************************************************************' \
                  '************************************************************' + '\n'

        result += f'*        {self.monday_jur[1]}        *      {self.tuesday_jur[1]}        *    ' \
                  f' {self.wednesday_jur[1]}      *         {self.thursday_jur[1]}         *     ' \
                  f' {self.friday_jur[1]}      *   {self.saturday_jur[1]}  *' + '\n'
        result += f'*          {self.monday_jur[2]}           *       {self.tuesday_jur[2]}         *      ' \
                  f'   {self.wednesday_jur[2]}         *            {self.thursday_jur[2]}           * ' \
                  f'       {self.friday_jur[2]}      *      {self.saturday_jur[2][:-1]}         *' + '\n'
        result += f'*          {self.monday_jur[3][:-1]}          *   {self.tuesday_jur[3]}     *   ' \
                  f'  {self.wednesday_jur[3][:-1]}      *         {self.thursday_jur[3][:-1]}       *   ' \
                  f'     {self.friday_jur[3]}      *            -           *' + '\n'
        result += f'*           -           *  {self.tuesday_jur[4][:-1]}  *            -          ' \
                  f'  *            -            *     {self.friday_jur[4]}      *            -        ' \
                  f'   *' + '\n'
        result += f'*           -           *           -           *            -            *          ' \
                  f'  -            *    {self.friday_jur[5][:-1]}   *            -           *' + '\n'
        result += '*************************************************************************************' \
                  '***************************************************************' + '\n'

        return result

    def __repr__(self):
        """Output method."""

        return self.__str__()

