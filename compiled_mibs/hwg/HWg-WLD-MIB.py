# SNMP MIB module (HWg-WLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\hwg\HWg-WLD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:00:05 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class SensorState(Integer32):
    """Custom type SensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("alarm", 3))
    )





class SensorValue(Integer32):
    """Custom type SensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("flooded", 1),
          ("disconnect", 2),
          ("invalid", 3))
    )





class SensorSN(DisplayString):
    """Custom type SensorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class SensorName(DisplayString):
    """Custom type SensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )





class SensorID(Integer32):
    """Custom type SensorID based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hwgroup_ObjectIdentity = ObjectIdentity
hwgroup = _Hwgroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796)
)
_X390_ObjectIdentity = ObjectIdentity
x390 = _X390_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4)
)
_Hwgwld_ObjectIdentity = ObjectIdentity
hwgwld = _Hwgwld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5)
)
_WldTable_Object = MibTable
wldTable = _WldTable_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4)
)
if mibBuilder.loadTexts:
    wldTable.setStatus("mandatory")
_WldEntry_Object = MibTableRow
wldEntry = _WldEntry_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1)
)
wldEntry.setIndexNames(
    (0, "HWg-WLD-MIB", "wldIndex"),
)
if mibBuilder.loadTexts:
    wldEntry.setStatus("mandatory")
_WldIndex_Type = PositiveInteger
_WldIndex_Object = MibTableColumn
wldIndex = _WldIndex_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 1),
    _WldIndex_Type()
)
wldIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wldIndex.setStatus("mandatory")
_WldName_Type = SensorName
_WldName_Object = MibTableColumn
wldName = _WldName_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 2),
    _WldName_Type()
)
wldName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wldName.setStatus("mandatory")
_WldState_Type = SensorState
_WldState_Object = MibTableColumn
wldState = _WldState_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 3),
    _WldState_Type()
)
wldState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wldState.setStatus("mandatory")
_WldSN_Type = SensorSN
_WldSN_Object = MibTableColumn
wldSN = _WldSN_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 4),
    _WldSN_Type()
)
wldSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wldSN.setStatus("mandatory")
_WldID_Type = SensorID
_WldID_Object = MibTableColumn
wldID = _WldID_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 5),
    _WldID_Type()
)
wldID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wldID.setStatus("mandatory")
_WldValue_Type = SensorValue
_WldValue_Object = MibTableColumn
wldValue = _WldValue_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 4, 1, 6),
    _WldValue_Type()
)
wldValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wldValue.setStatus("mandatory")
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 70)
)


class _InfoAddressMAC_Type(DisplayString):
    """Custom type infoAddressMAC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 17),
    )


_InfoAddressMAC_Type.__name__ = "DisplayString"
_InfoAddressMAC_Object = MibScalar
infoAddressMAC = _InfoAddressMAC_Object(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 70, 1),
    _InfoAddressMAC_Type()
)
infoAddressMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infoAddressMAC.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wldStateToAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 0, 1)
)
wldStateToAlarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("HWg-WLD-MIB", "infoAddressMAC"),
        ("HWg-WLD-MIB", "wldIndex"),
        ("HWg-WLD-MIB", "wldName"),
        ("HWg-WLD-MIB", "wldState"),
        ("HWg-WLD-MIB", "wldSN"),
        ("HWg-WLD-MIB", "wldID"),
        ("HWg-WLD-MIB", "wldValue"))
)
if mibBuilder.loadTexts:
    wldStateToAlarm.setStatus(
        ""
    )

wldStateToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 0, 2)
)
wldStateToNormal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("HWg-WLD-MIB", "infoAddressMAC"),
        ("HWg-WLD-MIB", "wldIndex"),
        ("HWg-WLD-MIB", "wldName"),
        ("HWg-WLD-MIB", "wldState"),
        ("HWg-WLD-MIB", "wldSN"),
        ("HWg-WLD-MIB", "wldID"),
        ("HWg-WLD-MIB", "wldValue"))
)
if mibBuilder.loadTexts:
    wldStateToNormal.setStatus(
        ""
    )

wldPeriodicAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 21796, 4, 5, 0, 3)
)
wldPeriodicAlarm.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("HWg-WLD-MIB", "infoAddressMAC"),
        ("HWg-WLD-MIB", "wldIndex"),
        ("HWg-WLD-MIB", "wldName"),
        ("HWg-WLD-MIB", "wldState"),
        ("HWg-WLD-MIB", "wldSN"),
        ("HWg-WLD-MIB", "wldID"),
        ("HWg-WLD-MIB", "wldValue"))
)
if mibBuilder.loadTexts:
    wldPeriodicAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HWg-WLD-MIB",
    **{"PositiveInteger": PositiveInteger,
       "SensorState": SensorState,
       "SensorValue": SensorValue,
       "SensorSN": SensorSN,
       "SensorName": SensorName,
       "SensorID": SensorID,
       "hwgroup": hwgroup,
       "x390": x390,
       "hwgwld": hwgwld,
       "wldStateToAlarm": wldStateToAlarm,
       "wldStateToNormal": wldStateToNormal,
       "wldPeriodicAlarm": wldPeriodicAlarm,
       "wldTable": wldTable,
       "wldEntry": wldEntry,
       "wldIndex": wldIndex,
       "wldName": wldName,
       "wldState": wldState,
       "wldSN": wldSN,
       "wldID": wldID,
       "wldValue": wldValue,
       "info": info,
       "infoAddressMAC": infoAddressMAC}
)
