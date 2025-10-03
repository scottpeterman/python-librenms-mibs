# SNMP MIB module (COLUBRIS-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hpmsm\COLUBRIS-SYSLOG-MIB.my
# Produced by pysmi-1.6.2 at Thu Oct  2 11:52:10 2025
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

(ColubrisNotificationEnable,) = mibBuilder.importSymbols(
    "COLUBRIS-TC",
    "ColubrisNotificationEnable")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

colubrisSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverity(TextualConvention, Integer32):
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



# MIB Managed Objects in the order of their OIDs

_ColubrisSyslogMIBObjects_ObjectIdentity = ObjectIdentity
colubrisSyslogMIBObjects = _ColubrisSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1)
)
_SyslogConfig_ObjectIdentity = ObjectIdentity
syslogConfig = _SyslogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1)
)


class _SyslogSeverityNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type syslogSeverityNotificationEnabled based on ColubrisNotificationEnable"""
    defaultValue = 1


_SyslogSeverityNotificationEnabled_Type.__name__ = "ColubrisNotificationEnable"
_SyslogSeverityNotificationEnabled_Object = MibScalar
syslogSeverityNotificationEnabled = _SyslogSeverityNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 1),
    _SyslogSeverityNotificationEnabled_Type()
)
syslogSeverityNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSeverityNotificationEnabled.setStatus("current")


class _SyslogRegExMatchNotificationEnabled_Type(ColubrisNotificationEnable):
    """Custom type syslogRegExMatchNotificationEnabled based on ColubrisNotificationEnable"""
    defaultValue = 2


_SyslogRegExMatchNotificationEnabled_Type.__name__ = "ColubrisNotificationEnable"
_SyslogRegExMatchNotificationEnabled_Object = MibScalar
syslogRegExMatchNotificationEnabled = _SyslogRegExMatchNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 2),
    _SyslogRegExMatchNotificationEnabled_Type()
)
syslogRegExMatchNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogRegExMatchNotificationEnabled.setStatus("current")


class _SyslogSeverityLevel_Type(SyslogSeverity):
    """Custom type syslogSeverityLevel based on SyslogSeverity"""
    defaultValue = 5


_SyslogSeverityLevel_Type.__name__ = "SyslogSeverity"
_SyslogSeverityLevel_Object = MibScalar
syslogSeverityLevel = _SyslogSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 3),
    _SyslogSeverityLevel_Type()
)
syslogSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSeverityLevel.setStatus("current")


class _SyslogTrapSeverityLevel_Type(SyslogSeverity):
    """Custom type syslogTrapSeverityLevel based on SyslogSeverity"""
    defaultValue = 5


_SyslogTrapSeverityLevel_Type.__name__ = "SyslogSeverity"
_SyslogTrapSeverityLevel_Object = MibScalar
syslogTrapSeverityLevel = _SyslogTrapSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 4),
    _SyslogTrapSeverityLevel_Type()
)
syslogTrapSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogTrapSeverityLevel.setStatus("current")
_SyslogMessageRegEx_Type = DisplayString
_SyslogMessageRegEx_Object = MibScalar
syslogMessageRegEx = _SyslogMessageRegEx_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 1, 5),
    _SyslogMessageRegEx_Type()
)
syslogMessageRegEx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMessageRegEx.setStatus("current")
_SyslogMessage_ObjectIdentity = ObjectIdentity
syslogMessage = _SyslogMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2)
)
_SyslogMsgNumber_Type = Unsigned32
_SyslogMsgNumber_Object = MibScalar
syslogMsgNumber = _SyslogMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 1),
    _SyslogMsgNumber_Type()
)
syslogMsgNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgNumber.setStatus("current")
_SyslogMsgFacility_Type = DisplayString
_SyslogMsgFacility_Object = MibScalar
syslogMsgFacility = _SyslogMsgFacility_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 2),
    _SyslogMsgFacility_Type()
)
syslogMsgFacility.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgFacility.setStatus("current")
_SyslogMsgSeverity_Type = SyslogSeverity
_SyslogMsgSeverity_Object = MibScalar
syslogMsgSeverity = _SyslogMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 3),
    _SyslogMsgSeverity_Type()
)
syslogMsgSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgSeverity.setStatus("current")
_SyslogMsgText_Type = DisplayString
_SyslogMsgText_Object = MibScalar
syslogMsgText = _SyslogMsgText_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 1, 2, 4),
    _SyslogMsgText_Type()
)
syslogMsgText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgText.setStatus("current")
_ColubrisSyslogMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisSyslogMIBNotificationPrefix = _ColubrisSyslogMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 2)
)
_ColubrisSyslogMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisSyslogMIBNotifications = _ColubrisSyslogMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0)
)
_ColubrisSyslogMIBConformance_ObjectIdentity = ObjectIdentity
colubrisSyslogMIBConformance = _ColubrisSyslogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 3)
)
_ColubrisSyslogMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisSyslogMIBCompliances = _ColubrisSyslogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 1)
)
_ColubrisSyslogMIBGroups_ObjectIdentity = ObjectIdentity
colubrisSyslogMIBGroups = _ColubrisSyslogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2)
)

# Managed Objects groups

colubrisSyslogMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2, 1)
)
colubrisSyslogMIBGroup.setObjects(
      *(("COLUBRIS-SYSLOG-MIB", "syslogSeverityNotificationEnabled"),
        ("COLUBRIS-SYSLOG-MIB", "syslogRegExMatchNotificationEnabled"),
        ("COLUBRIS-SYSLOG-MIB", "syslogSeverityLevel"),
        ("COLUBRIS-SYSLOG-MIB", "syslogTrapSeverityLevel"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMessageRegEx"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
)
if mibBuilder.loadTexts:
    colubrisSyslogMIBGroup.setStatus("current")


# Notification objects

syslogSeverityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0, 1)
)
syslogSeverityNotification.setObjects(
      *(("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
)
if mibBuilder.loadTexts:
    syslogSeverityNotification.setStatus(
        "current"
    )

syslogRegExMatchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 2, 0, 2)
)
syslogRegExMatchNotification.setObjects(
      *(("COLUBRIS-SYSLOG-MIB", "syslogMsgNumber"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgFacility"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgSeverity"),
        ("COLUBRIS-SYSLOG-MIB", "syslogMsgText"))
)
if mibBuilder.loadTexts:
    syslogRegExMatchNotification.setStatus(
        "current"
    )


# Notifications groups

colubrisSyslogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 2, 2)
)
colubrisSyslogNotificationGroup.setObjects(
      *(("COLUBRIS-SYSLOG-MIB", "syslogSeverityNotification"),
        ("COLUBRIS-SYSLOG-MIB", "syslogRegExMatchNotification"))
)
if mibBuilder.loadTexts:
    colubrisSyslogNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

colubrisSyslogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 3, 3, 1, 1)
)
colubrisSyslogMIBCompliance.setObjects(
      *(("COLUBRIS-SYSLOG-MIB", "colubrisSyslogMIBGroup"),
        ("COLUBRIS-SYSLOG-MIB", "colubrisSyslogNotificationGroup"))
)
if mibBuilder.loadTexts:
    colubrisSyslogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-SYSLOG-MIB",
    **{"SyslogSeverity": SyslogSeverity,
       "colubrisSyslogMIB": colubrisSyslogMIB,
       "colubrisSyslogMIBObjects": colubrisSyslogMIBObjects,
       "syslogConfig": syslogConfig,
       "syslogSeverityNotificationEnabled": syslogSeverityNotificationEnabled,
       "syslogRegExMatchNotificationEnabled": syslogRegExMatchNotificationEnabled,
       "syslogSeverityLevel": syslogSeverityLevel,
       "syslogTrapSeverityLevel": syslogTrapSeverityLevel,
       "syslogMessageRegEx": syslogMessageRegEx,
       "syslogMessage": syslogMessage,
       "syslogMsgNumber": syslogMsgNumber,
       "syslogMsgFacility": syslogMsgFacility,
       "syslogMsgSeverity": syslogMsgSeverity,
       "syslogMsgText": syslogMsgText,
       "colubrisSyslogMIBNotificationPrefix": colubrisSyslogMIBNotificationPrefix,
       "colubrisSyslogMIBNotifications": colubrisSyslogMIBNotifications,
       "syslogSeverityNotification": syslogSeverityNotification,
       "syslogRegExMatchNotification": syslogRegExMatchNotification,
       "colubrisSyslogMIBConformance": colubrisSyslogMIBConformance,
       "colubrisSyslogMIBCompliances": colubrisSyslogMIBCompliances,
       "colubrisSyslogMIBCompliance": colubrisSyslogMIBCompliance,
       "colubrisSyslogMIBGroups": colubrisSyslogMIBGroups,
       "colubrisSyslogMIBGroup": colubrisSyslogMIBGroup,
       "colubrisSyslogNotificationGroup": colubrisSyslogNotificationGroup}
)
