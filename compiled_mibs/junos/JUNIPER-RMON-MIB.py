# SNMP MIB module (JUNIPER-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-RMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:04:34 2025
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
 jnxRmonTraps) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs",
    "jnxRmonTraps")

(alarmEntry,
 alarmIndex,
 alarmVariable) = mibBuilder.importSymbols(
    "RMON-MIB",
    "alarmEntry",
    "alarmIndex",
    "alarmVariable")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxRmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13)
)
if mibBuilder.loadTexts:
    jnxRmon.setRevisions(
        ("2005-11-23 00:00",
         "2002-01-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxRmonAlarmTable_Object = MibTable
jnxRmonAlarmTable = _JnxRmonAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13, 1)
)
if mibBuilder.loadTexts:
    jnxRmonAlarmTable.setStatus("current")
_JnxRmonAlarmEntry_Object = MibTableRow
jnxRmonAlarmEntry = _JnxRmonAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13, 1, 1)
)
if mibBuilder.loadTexts:
    jnxRmonAlarmEntry.setStatus("current")
_JnxRmonAlarmGetFailCnt_Type = Counter32
_JnxRmonAlarmGetFailCnt_Object = MibTableColumn
jnxRmonAlarmGetFailCnt = _JnxRmonAlarmGetFailCnt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13, 1, 1, 1),
    _JnxRmonAlarmGetFailCnt_Type()
)
jnxRmonAlarmGetFailCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRmonAlarmGetFailCnt.setStatus("current")
_JnxRmonAlarmGetFailTime_Type = TimeTicks
_JnxRmonAlarmGetFailTime_Object = MibTableColumn
jnxRmonAlarmGetFailTime = _JnxRmonAlarmGetFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13, 1, 1, 2),
    _JnxRmonAlarmGetFailTime_Type()
)
jnxRmonAlarmGetFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRmonAlarmGetFailTime.setStatus("current")


class _JnxRmonAlarmGetFailReason_Type(Integer32):
    """Custom type jnxRmonAlarmGetFailReason based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noError", 2),
          ("noSuchObject", 3),
          ("outOfView", 4),
          ("noSuchInstance", 5),
          ("badReqId", 6),
          ("oidMatchErr", 7),
          ("oidBindErr", 8),
          ("createPktErr", 9),
          ("badObjType", 10),
          ("processRestarted", 11),
          ("lostInstance", 12))
    )


_JnxRmonAlarmGetFailReason_Type.__name__ = "Integer32"
_JnxRmonAlarmGetFailReason_Object = MibTableColumn
jnxRmonAlarmGetFailReason = _JnxRmonAlarmGetFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13, 1, 1, 3),
    _JnxRmonAlarmGetFailReason_Type()
)
jnxRmonAlarmGetFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRmonAlarmGetFailReason.setStatus("current")
_JnxRmonAlarmGetOkTime_Type = TimeTicks
_JnxRmonAlarmGetOkTime_Object = MibTableColumn
jnxRmonAlarmGetOkTime = _JnxRmonAlarmGetOkTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13, 1, 1, 4),
    _JnxRmonAlarmGetOkTime_Type()
)
jnxRmonAlarmGetOkTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRmonAlarmGetOkTime.setStatus("current")


class _JnxRmonAlarmState_Type(Integer32):
    """Custom type jnxRmonAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("underCreation", 2),
          ("active", 3),
          ("startup", 4),
          ("risingThreshold", 5),
          ("fallingThreshold", 6),
          ("getFailure", 7))
    )


_JnxRmonAlarmState_Type.__name__ = "Integer32"
_JnxRmonAlarmState_Object = MibTableColumn
jnxRmonAlarmState = _JnxRmonAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 13, 1, 1, 5),
    _JnxRmonAlarmState_Type()
)
jnxRmonAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxRmonAlarmState.setStatus("current")
_JnxRmonTrapPrefix_ObjectIdentity = ObjectIdentity
jnxRmonTrapPrefix = _JnxRmonTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 3, 0)
)
alarmEntry.registerAugmentions(
    ("JUNIPER-RMON-MIB",
     "jnxRmonAlarmEntry")
)
jnxRmonAlarmEntry.setIndexNames(*alarmEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxRmonAlarmGetFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 3, 0, 1)
)
jnxRmonAlarmGetFailure.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmVariable"),
        ("JUNIPER-RMON-MIB", "jnxRmonAlarmGetFailReason"))
)
if mibBuilder.loadTexts:
    jnxRmonAlarmGetFailure.setStatus(
        "current"
    )

jnxRmonGetOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 4, 3, 0, 2)
)
jnxRmonGetOk.setObjects(
      *(("RMON-MIB", "alarmIndex"),
        ("RMON-MIB", "alarmVariable"))
)
if mibBuilder.loadTexts:
    jnxRmonGetOk.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-RMON-MIB",
    **{"jnxRmon": jnxRmon,
       "jnxRmonAlarmTable": jnxRmonAlarmTable,
       "jnxRmonAlarmEntry": jnxRmonAlarmEntry,
       "jnxRmonAlarmGetFailCnt": jnxRmonAlarmGetFailCnt,
       "jnxRmonAlarmGetFailTime": jnxRmonAlarmGetFailTime,
       "jnxRmonAlarmGetFailReason": jnxRmonAlarmGetFailReason,
       "jnxRmonAlarmGetOkTime": jnxRmonAlarmGetOkTime,
       "jnxRmonAlarmState": jnxRmonAlarmState,
       "jnxRmonTrapPrefix": jnxRmonTrapPrefix,
       "jnxRmonAlarmGetFailure": jnxRmonAlarmGetFailure,
       "jnxRmonGetOk": jnxRmonGetOk}
)
