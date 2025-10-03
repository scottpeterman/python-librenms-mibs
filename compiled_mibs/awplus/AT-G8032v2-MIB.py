# SNMP MIB module (AT-G8032v2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-G8032v2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:27 2025
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atG8032v2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604)
)
if mibBuilder.loadTexts:
    atG8032v2.setRevisions(
        ("2017-02-06 00:00",
         "2017-01-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AtG8032v2InstanceState(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("init", 2),
          ("idle", 3),
          ("protection", 4),
          ("manualSwitch", 5),
          ("forcedSwitch", 6),
          ("pending", 7))
    )



# MIB Managed Objects in the order of their OIDs

_AtG8032v2Notifications_ObjectIdentity = ObjectIdentity
atG8032v2Notifications = _AtG8032v2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0)
)
_AtG8032v2NotificationVariable_ObjectIdentity = ObjectIdentity
atG8032v2NotificationVariable = _AtG8032v2NotificationVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1)
)


class _AtG8032v2NotificationInstanceName_Type(DisplayStringUnsized):
    """Custom type atG8032v2NotificationInstanceName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtG8032v2NotificationInstanceName_Type.__name__ = "DisplayStringUnsized"
_AtG8032v2NotificationInstanceName_Object = MibScalar
atG8032v2NotificationInstanceName = _AtG8032v2NotificationInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 1),
    _AtG8032v2NotificationInstanceName_Type()
)
atG8032v2NotificationInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atG8032v2NotificationInstanceName.setStatus("current")
_AtG8032v2NotificationInstanceFromState_Type = AtG8032v2InstanceState
_AtG8032v2NotificationInstanceFromState_Object = MibScalar
atG8032v2NotificationInstanceFromState = _AtG8032v2NotificationInstanceFromState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 2),
    _AtG8032v2NotificationInstanceFromState_Type()
)
atG8032v2NotificationInstanceFromState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atG8032v2NotificationInstanceFromState.setStatus("current")
_AtG8032v2NotificationInstanceCurrentState_Type = AtG8032v2InstanceState
_AtG8032v2NotificationInstanceCurrentState_Object = MibScalar
atG8032v2NotificationInstanceCurrentState = _AtG8032v2NotificationInstanceCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 3),
    _AtG8032v2NotificationInstanceCurrentState_Type()
)
atG8032v2NotificationInstanceCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atG8032v2NotificationInstanceCurrentState.setStatus("current")
_AtG8032v2NotificationSystemAlarmState_Type = TruthValue
_AtG8032v2NotificationSystemAlarmState_Object = MibScalar
atG8032v2NotificationSystemAlarmState = _AtG8032v2NotificationSystemAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 1, 4),
    _AtG8032v2NotificationSystemAlarmState_Type()
)
atG8032v2NotificationSystemAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atG8032v2NotificationSystemAlarmState.setStatus("current")

# Managed Objects groups


# Notification objects

atG8032v2InstanceNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0, 1)
)
atG8032v2InstanceNotify.setObjects(
      *(("AT-G8032v2-MIB", "atG8032v2NotificationInstanceName"),
        ("AT-G8032v2-MIB", "atG8032v2NotificationInstanceFromState"),
        ("AT-G8032v2-MIB", "atG8032v2NotificationInstanceCurrentState"))
)
if mibBuilder.loadTexts:
    atG8032v2InstanceNotify.setStatus(
        "current"
    )

atG8032v2SystemAlarmNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 604, 0, 2)
)
atG8032v2SystemAlarmNotify.setObjects(
    ("AT-G8032v2-MIB", "atG8032v2NotificationSystemAlarmState")
)
if mibBuilder.loadTexts:
    atG8032v2SystemAlarmNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-G8032v2-MIB",
    **{"AtG8032v2InstanceState": AtG8032v2InstanceState,
       "atG8032v2": atG8032v2,
       "atG8032v2Notifications": atG8032v2Notifications,
       "atG8032v2InstanceNotify": atG8032v2InstanceNotify,
       "atG8032v2SystemAlarmNotify": atG8032v2SystemAlarmNotify,
       "atG8032v2NotificationVariable": atG8032v2NotificationVariable,
       "atG8032v2NotificationInstanceName": atG8032v2NotificationInstanceName,
       "atG8032v2NotificationInstanceFromState": atG8032v2NotificationInstanceFromState,
       "atG8032v2NotificationInstanceCurrentState": atG8032v2NotificationInstanceCurrentState,
       "atG8032v2NotificationSystemAlarmState": atG8032v2NotificationSystemAlarmState}
)
