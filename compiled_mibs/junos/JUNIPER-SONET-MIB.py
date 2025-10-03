# SNMP MIB module (JUNIPER-SONET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-SONET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:48 2025
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

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(jnxMibs,
 jnxSonetNotifications) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxSonetNotifications")

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

jnxSonet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20)
)
if mibBuilder.loadTexts:
    jnxSonet.setRevisions(
        ("2002-12-12 00:00",
         "2002-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxSonetAlarmId(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("sonetLolAlarm", 0),
          ("sonetPllAlarm", 1),
          ("sonetLofAlarm", 2),
          ("sonetLosAlarm", 3),
          ("sonetSefAlarm", 4),
          ("sonetLaisAlarm", 5),
          ("sonetPaisAlarm", 6),
          ("sonetLopAlarm", 7),
          ("sonetBerrSdAlarm", 8),
          ("sonetBerrSfAlarm", 9),
          ("sonetLrdiAlarm", 10),
          ("sonetPrdiAlarm", 11),
          ("sonetReiAlarm", 12),
          ("sonetUneqAlarm", 13),
          ("sonetPmisAlarm", 14),
          ("sonetLocAlarm", 15),
          ("sonetVaisAlarm", 16),
          ("sonetVlopAlarm", 17),
          ("sonetVrdiAlarm", 18),
          ("sonetVuneqAlarm", 19),
          ("sonetVmisAlarm", 20),
          ("sonetVlocAlarm", 21),
          ("sdhLolAlarm", 22),
          ("sdhPllAlarm", 23),
          ("sdhLofAlarm", 24),
          ("sdhLosAlarm", 25),
          ("sdhOofAlarm", 26),
          ("sdhMsAisAlarm", 27),
          ("sdhHpAisAlarm", 28),
          ("sdhLopAlarm", 29),
          ("sdhBerrSdAlarm", 30),
          ("sdhBerrSfAlarm", 31),
          ("sdhMsFerfAlarm", 32),
          ("sdhHpFerfAlarm", 33),
          ("sdhMsFebeAlarm", 34),
          ("sdhHpUneqAlarm", 35),
          ("sdhHpMisAlarm", 36),
          ("sdhLocAlarm", 37))
    )


# MIB Managed Objects in the order of their OIDs

_JnxSonetAlarms_ObjectIdentity = ObjectIdentity
jnxSonetAlarms = _JnxSonetAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1)
)
_JnxSonetAlarmTable_Object = MibTable
jnxSonetAlarmTable = _JnxSonetAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSonetAlarmTable.setStatus("current")
_JnxSonetAlarmEntry_Object = MibTableRow
jnxSonetAlarmEntry = _JnxSonetAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1)
)
jnxSonetAlarmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxSonetAlarmEntry.setStatus("current")
_JnxSonetCurrentAlarms_Type = JnxSonetAlarmId
_JnxSonetCurrentAlarms_Object = MibTableColumn
jnxSonetCurrentAlarms = _JnxSonetCurrentAlarms_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 1),
    _JnxSonetCurrentAlarms_Type()
)
jnxSonetCurrentAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetCurrentAlarms.setStatus("current")
_JnxSonetLastAlarmId_Type = JnxSonetAlarmId
_JnxSonetLastAlarmId_Object = MibTableColumn
jnxSonetLastAlarmId = _JnxSonetLastAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 2),
    _JnxSonetLastAlarmId_Type()
)
jnxSonetLastAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmId.setStatus("current")
_JnxSonetLastAlarmTime_Type = TimeTicks
_JnxSonetLastAlarmTime_Object = MibTableColumn
jnxSonetLastAlarmTime = _JnxSonetLastAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 3),
    _JnxSonetLastAlarmTime_Type()
)
jnxSonetLastAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmTime.setStatus("current")
_JnxSonetLastAlarmDate_Type = DateAndTime
_JnxSonetLastAlarmDate_Object = MibTableColumn
jnxSonetLastAlarmDate = _JnxSonetLastAlarmDate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 4),
    _JnxSonetLastAlarmDate_Type()
)
jnxSonetLastAlarmDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmDate.setStatus("current")


class _JnxSonetLastAlarmEvent_Type(Integer32):
    """Custom type jnxSonetLastAlarmEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("set", 2),
          ("cleared", 3))
    )


_JnxSonetLastAlarmEvent_Type.__name__ = "Integer32"
_JnxSonetLastAlarmEvent_Object = MibTableColumn
jnxSonetLastAlarmEvent = _JnxSonetLastAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 20, 1, 1, 1, 5),
    _JnxSonetLastAlarmEvent_Type()
)
jnxSonetLastAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxSonetLastAlarmEvent.setStatus("current")
_JnxSonetNotificationPrefix_ObjectIdentity = ObjectIdentity
jnxSonetNotificationPrefix = _JnxSonetNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6, 0)
)

# Managed Objects groups


# Notification objects

jnxSonetAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 1)
)
jnxSonetAlarmSet.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"),
        ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxSonetAlarmSet.setStatus(
        "current"
    )

jnxSonetAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6, 0, 2)
)
jnxSonetAlarmCleared.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmId"),
        ("JUNIPER-SONET-MIB", "jnxSonetCurrentAlarms"),
        ("JUNIPER-SONET-MIB", "jnxSonetLastAlarmDate"))
)
if mibBuilder.loadTexts:
    jnxSonetAlarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SONET-MIB",
    **{"JnxSonetAlarmId": JnxSonetAlarmId,
       "jnxSonet": jnxSonet,
       "jnxSonetAlarms": jnxSonetAlarms,
       "jnxSonetAlarmTable": jnxSonetAlarmTable,
       "jnxSonetAlarmEntry": jnxSonetAlarmEntry,
       "jnxSonetCurrentAlarms": jnxSonetCurrentAlarms,
       "jnxSonetLastAlarmId": jnxSonetLastAlarmId,
       "jnxSonetLastAlarmTime": jnxSonetLastAlarmTime,
       "jnxSonetLastAlarmDate": jnxSonetLastAlarmDate,
       "jnxSonetLastAlarmEvent": jnxSonetLastAlarmEvent,
       "jnxSonetNotificationPrefix": jnxSonetNotificationPrefix,
       "jnxSonetAlarmSet": jnxSonetAlarmSet,
       "jnxSonetAlarmCleared": jnxSonetAlarmCleared}
)
