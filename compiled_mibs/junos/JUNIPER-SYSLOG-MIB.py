# SNMP MIB module (JUNIPER-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:53 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(jnxMibs,
 jnxSyslogNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxSyslogNotifications")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxSyslog = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxSyslogSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )



class JnxSyslogFacility(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 1),
          ("user", 2),
          ("mail", 3),
          ("daemon", 4),
          ("auth", 5),
          ("syslog", 6),
          ("lpr", 7),
          ("news", 8),
          ("uucp", 9),
          ("cron", 10),
          ("authPriv", 11),
          ("ftp", 12),
          ("ntp", 13),
          ("security", 14),
          ("console", 15),
          ("local0", 17),
          ("dfc", 18),
          ("local2", 19),
          ("firewall", 20),
          ("pfe", 21),
          ("conflict", 22),
          ("change", 23),
          ("interact", 24))
    )



# MIB Managed Objects in the order of their OIDs

_JnxSyslogNotifyVars_ObjectIdentity = ObjectIdentity
jnxSyslogNotifyVars = _JnxSyslogNotifyVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1)
)
if mibBuilder.loadTexts:
    jnxSyslogNotifyVars.setStatus("current")
_JnxSyslogTable_Object = MibTable
jnxSyslogTable = _JnxSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSyslogTable.setStatus("current")
_JnxSyslogEntry_Object = MibTableRow
jnxSyslogEntry = _JnxSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1)
)
jnxSyslogEntry.setIndexNames(
    (0, "JUNIPER-SYSLOG-MIB", "jnxSyslogId"),
)
if mibBuilder.loadTexts:
    jnxSyslogEntry.setStatus("current")
_JnxSyslogId_Type = Unsigned32
_JnxSyslogId_Object = MibTableColumn
jnxSyslogId = _JnxSyslogId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 1),
    _JnxSyslogId_Type()
)
jnxSyslogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSyslogId.setStatus("current")
_JnxSyslogEventName_Type = DisplayString
_JnxSyslogEventName_Object = MibTableColumn
jnxSyslogEventName = _JnxSyslogEventName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 2),
    _JnxSyslogEventName_Type()
)
jnxSyslogEventName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogEventName.setStatus("current")
_JnxSyslogTimestamp_Type = DateAndTime
_JnxSyslogTimestamp_Object = MibTableColumn
jnxSyslogTimestamp = _JnxSyslogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 3),
    _JnxSyslogTimestamp_Type()
)
jnxSyslogTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogTimestamp.setStatus("current")
_JnxSyslogSeverity_Type = JnxSyslogSeverity
_JnxSyslogSeverity_Object = MibTableColumn
jnxSyslogSeverity = _JnxSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 4),
    _JnxSyslogSeverity_Type()
)
jnxSyslogSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogSeverity.setStatus("current")
_JnxSyslogFacility_Type = JnxSyslogFacility
_JnxSyslogFacility_Object = MibTableColumn
jnxSyslogFacility = _JnxSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 5),
    _JnxSyslogFacility_Type()
)
jnxSyslogFacility.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogFacility.setStatus("current")
_JnxSyslogProcessId_Type = Unsigned32
_JnxSyslogProcessId_Object = MibTableColumn
jnxSyslogProcessId = _JnxSyslogProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 6),
    _JnxSyslogProcessId_Type()
)
jnxSyslogProcessId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogProcessId.setStatus("current")
_JnxSyslogProcessName_Type = DisplayString
_JnxSyslogProcessName_Object = MibTableColumn
jnxSyslogProcessName = _JnxSyslogProcessName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 7),
    _JnxSyslogProcessName_Type()
)
jnxSyslogProcessName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogProcessName.setStatus("current")
_JnxSyslogHostName_Type = DisplayString
_JnxSyslogHostName_Object = MibTableColumn
jnxSyslogHostName = _JnxSyslogHostName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 8),
    _JnxSyslogHostName_Type()
)
jnxSyslogHostName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogHostName.setStatus("current")
_JnxSyslogMessage_Type = OctetString
_JnxSyslogMessage_Object = MibTableColumn
jnxSyslogMessage = _JnxSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 1, 1, 9),
    _JnxSyslogMessage_Type()
)
jnxSyslogMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogMessage.setStatus("current")
_JnxSyslogAvTable_Object = MibTable
jnxSyslogAvTable = _JnxSyslogAvTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2)
)
if mibBuilder.loadTexts:
    jnxSyslogAvTable.setStatus("current")
_JnxSyslogAvEntry_Object = MibTableRow
jnxSyslogAvEntry = _JnxSyslogAvEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1)
)
jnxSyslogAvEntry.setIndexNames(
    (0, "JUNIPER-SYSLOG-MIB", "jnxSyslogId"),
    (0, "JUNIPER-SYSLOG-MIB", "jnxSyslogAvIndex"),
)
if mibBuilder.loadTexts:
    jnxSyslogAvEntry.setStatus("current")
_JnxSyslogAvIndex_Type = Unsigned32
_JnxSyslogAvIndex_Object = MibTableColumn
jnxSyslogAvIndex = _JnxSyslogAvIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 1),
    _JnxSyslogAvIndex_Type()
)
jnxSyslogAvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxSyslogAvIndex.setStatus("current")
_JnxSyslogAvAttribute_Type = DisplayString
_JnxSyslogAvAttribute_Object = MibTableColumn
jnxSyslogAvAttribute = _JnxSyslogAvAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 2),
    _JnxSyslogAvAttribute_Type()
)
jnxSyslogAvAttribute.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogAvAttribute.setStatus("current")
_JnxSyslogAvValue_Type = DisplayString
_JnxSyslogAvValue_Object = MibTableColumn
jnxSyslogAvValue = _JnxSyslogAvValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 2, 1, 3),
    _JnxSyslogAvValue_Type()
)
jnxSyslogAvValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxSyslogAvValue.setStatus("current")
_JnxUserDefinedTrapOID_Type = ObjectIdentifier
_JnxUserDefinedTrapOID_Object = MibScalar
jnxUserDefinedTrapOID = _JnxUserDefinedTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 35, 1, 3),
    _JnxUserDefinedTrapOID_Type()
)
jnxUserDefinedTrapOID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxUserDefinedTrapOID.setStatus("current")
_JnxSyslogNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxSyslogNotificationPrefix = _JnxSyslogNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0)
)
if mibBuilder.loadTexts:
    jnxSyslogNotificationPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

jnxSyslogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 1)
)
jnxSyslogTrap.setObjects(
      *(("JUNIPER-SYSLOG-MIB", "jnxSyslogEventName"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogTimestamp"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogSeverity"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogFacility"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogProcessId"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogProcessName"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogHostName"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogMessage"))
)
if mibBuilder.loadTexts:
    jnxSyslogTrap.setStatus(
        "current"
    )

jnxUserDefinedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 12, 0, 2)
)
jnxUserDefinedNotification.setObjects(
      *(("JUNIPER-SYSLOG-MIB", "jnxUserDefinedTrapOID"),
        ("JUNIPER-SYSLOG-MIB", "jnxSyslogMessage"))
)
if mibBuilder.loadTexts:
    jnxUserDefinedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SYSLOG-MIB",
    **{"JnxSyslogSeverity": JnxSyslogSeverity,
       "JnxSyslogFacility": JnxSyslogFacility,
       "jnxSyslog": jnxSyslog,
       "jnxSyslogNotifyVars": jnxSyslogNotifyVars,
       "jnxSyslogTable": jnxSyslogTable,
       "jnxSyslogEntry": jnxSyslogEntry,
       "jnxSyslogId": jnxSyslogId,
       "jnxSyslogEventName": jnxSyslogEventName,
       "jnxSyslogTimestamp": jnxSyslogTimestamp,
       "jnxSyslogSeverity": jnxSyslogSeverity,
       "jnxSyslogFacility": jnxSyslogFacility,
       "jnxSyslogProcessId": jnxSyslogProcessId,
       "jnxSyslogProcessName": jnxSyslogProcessName,
       "jnxSyslogHostName": jnxSyslogHostName,
       "jnxSyslogMessage": jnxSyslogMessage,
       "jnxSyslogAvTable": jnxSyslogAvTable,
       "jnxSyslogAvEntry": jnxSyslogAvEntry,
       "jnxSyslogAvIndex": jnxSyslogAvIndex,
       "jnxSyslogAvAttribute": jnxSyslogAvAttribute,
       "jnxSyslogAvValue": jnxSyslogAvValue,
       "jnxUserDefinedTrapOID": jnxUserDefinedTrapOID,
       "jnxSyslogNotificationPrefix": jnxSyslogNotificationPrefix,
       "jnxSyslogTrap": jnxSyslogTrap,
       "jnxUserDefinedNotification": jnxUserDefinedNotification}
)
