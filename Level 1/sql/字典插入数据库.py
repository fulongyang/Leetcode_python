









from pymysql import IntegrityError

class InsertMysqlDict():
    '''字典插入Mysql 通用类'''
    def __init__(self):
        self.cursor = ''
        self.conn = ''


    def insert_databases(self, table_name, table_source):
        error_list = []
        try:
            if isinstance(table_source, list):
                for table_dict in table_source:
                    # ------------------插入测试库
                    a = ','.join('{}'.format(key) for key in table_dict.keys())
                    b = ','.join("'{}'".format(value) for value in table_dict.values())
                    insert_dict = "INSERT INTO {} ({})VALUES({})".format(table_name, a, b);

                    self.cursor.execute(insert_dict)
                self.conn.commit()
                print('commit ok for {}'.format(table_name))
            elif isinstance(table_source, dict):
                a = ','.join('{}'.format(key) for key in table_source.keys())
                b = ','.join("'{}'".format(value) for value in table_source.values())
                insert_dict = "INSERT INTO {} ({})VALUES({})".format(table_name, a, b);
                self.cursor.execute(insert_dict)
                print('commit ok for {}'.format(table_name))
            self.conn.commit()

            # -----本地库提交
        except IntegrityError as e:
            print("Error: {}".format(e))
            error_list.append('{}'.format(e))
        # except Exception as e:
        #     print("Error: {}".format(e))
        insert_status = {
            'code': '{}'.format(200 if len(error_list) < 1 else 300),
            'insert_status': '{}'.format(''.join(error_list if error_list else 'ok')),
        }
        print('insert database ok.')
        return insert_status



