# SNMP MIB module (HH3C-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-AAA-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:41 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cAAA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181)
)
if mibBuilder.loadTexts:
    hh3cAAA.setRevisions(
        ("2020-01-13 00:00",
         "2019-03-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cAAAMibTrap_ObjectIdentity = ObjectIdentity
hh3cAAAMibTrap = _Hh3cAAAMibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1)
)
_Hh3cAAAMibTrapOid_ObjectIdentity = ObjectIdentity
hh3cAAAMibTrapOid = _Hh3cAAAMibTrapOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 1)
)
_Hh3cAAATrapOidDefine_ObjectIdentity = ObjectIdentity
hh3cAAATrapOidDefine = _Hh3cAAATrapOidDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 1, 1)
)
_Hh3cAAAUserChassis_Type = Integer32
_Hh3cAAAUserChassis_Object = MibScalar
hh3cAAAUserChassis = _Hh3cAAAUserChassis_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 1, 1, 1),
    _Hh3cAAAUserChassis_Type()
)
hh3cAAAUserChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAAAUserChassis.setStatus("current")
_Hh3cAAAUserSlot_Type = Integer32
_Hh3cAAAUserSlot_Object = MibScalar
hh3cAAAUserSlot = _Hh3cAAAUserSlot_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 1, 1, 2),
    _Hh3cAAAUserSlot_Type()
)
hh3cAAAUserSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAAAUserSlot.setStatus("current")
_Hh3cAAAUserSlotMaxNumThreshold_Type = Integer32
_Hh3cAAAUserSlotMaxNumThreshold_Object = MibScalar
hh3cAAAUserSlotMaxNumThreshold = _Hh3cAAAUserSlotMaxNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 1, 1, 3),
    _Hh3cAAAUserSlotMaxNumThreshold_Type()
)
hh3cAAAUserSlotMaxNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cAAAUserSlotMaxNumThreshold.setStatus("current")
_Hh3cAAATraps_ObjectIdentity = ObjectIdentity
hh3cAAATraps = _Hh3cAAATraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 2)
)
_Hh3cAAATrapsDefine_ObjectIdentity = ObjectIdentity
hh3cAAATrapsDefine = _Hh3cAAATrapsDefine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 2, 0)
)
_Hh3cAAATables_ObjectIdentity = ObjectIdentity
hh3cAAATables = _Hh3cAAATables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 2)
)
_Hh3cAAASlotStatTable_Object = MibTable
hh3cAAASlotStatTable = _Hh3cAAASlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cAAASlotStatTable.setStatus("current")
_Hh3cAAASlotStatEntry_Object = MibTableRow
hh3cAAASlotStatEntry = _Hh3cAAASlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 2, 1, 1)
)
hh3cAAASlotStatEntry.setIndexNames(
    (0, "HH3C-AAA-MIB", "hh3cAAAChassisId"),
    (0, "HH3C-AAA-MIB", "hh3cAAASlotId"),
)
if mibBuilder.loadTexts:
    hh3cAAASlotStatEntry.setStatus("current")


class _Hh3cAAAChassisId_Type(Unsigned32):
    """Custom type hh3cAAAChassisId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cAAAChassisId_Type.__name__ = "Unsigned32"
_Hh3cAAAChassisId_Object = MibTableColumn
hh3cAAAChassisId = _Hh3cAAAChassisId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 2, 1, 1, 1),
    _Hh3cAAAChassisId_Type()
)
hh3cAAAChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAAAChassisId.setStatus("current")
_Hh3cAAASlotId_Type = Unsigned32
_Hh3cAAASlotId_Object = MibTableColumn
hh3cAAASlotId = _Hh3cAAASlotId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 2, 1, 1, 2),
    _Hh3cAAASlotId_Type()
)
hh3cAAASlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cAAASlotId.setStatus("current")
_Hh3cAAASlotSessionResourceNum_Type = Unsigned32
_Hh3cAAASlotSessionResourceNum_Object = MibTableColumn
hh3cAAASlotSessionResourceNum = _Hh3cAAASlotSessionResourceNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 2, 1, 1, 3),
    _Hh3cAAASlotSessionResourceNum_Type()
)
hh3cAAASlotSessionResourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cAAASlotSessionResourceNum.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cAAAUserSlotMaxNum = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 2, 0, 1)
)
hh3cAAAUserSlotMaxNum.setObjects(
      *(("HH3C-AAA-MIB", "hh3cAAAUserChassis"),
        ("HH3C-AAA-MIB", "hh3cAAAUserSlot"),
        ("HH3C-AAA-MIB", "hh3cAAAUserSlotMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hh3cAAAUserSlotMaxNum.setStatus(
        "current"
    )

hh3cAAAUserSlotMaxNumResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 181, 1, 2, 0, 2)
)
hh3cAAAUserSlotMaxNumResume.setObjects(
      *(("HH3C-AAA-MIB", "hh3cAAAUserChassis"),
        ("HH3C-AAA-MIB", "hh3cAAAUserSlot"),
        ("HH3C-AAA-MIB", "hh3cAAAUserSlotMaxNumThreshold"))
)
if mibBuilder.loadTexts:
    hh3cAAAUserSlotMaxNumResume.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-AAA-MIB",
    **{"hh3cAAA": hh3cAAA,
       "hh3cAAAMibTrap": hh3cAAAMibTrap,
       "hh3cAAAMibTrapOid": hh3cAAAMibTrapOid,
       "hh3cAAATrapOidDefine": hh3cAAATrapOidDefine,
       "hh3cAAAUserChassis": hh3cAAAUserChassis,
       "hh3cAAAUserSlot": hh3cAAAUserSlot,
       "hh3cAAAUserSlotMaxNumThreshold": hh3cAAAUserSlotMaxNumThreshold,
       "hh3cAAATraps": hh3cAAATraps,
       "hh3cAAATrapsDefine": hh3cAAATrapsDefine,
       "hh3cAAAUserSlotMaxNum": hh3cAAAUserSlotMaxNum,
       "hh3cAAAUserSlotMaxNumResume": hh3cAAAUserSlotMaxNumResume,
       "hh3cAAATables": hh3cAAATables,
       "hh3cAAASlotStatTable": hh3cAAASlotStatTable,
       "hh3cAAASlotStatEntry": hh3cAAASlotStatEntry,
       "hh3cAAAChassisId": hh3cAAAChassisId,
       "hh3cAAASlotId": hh3cAAASlotId,
       "hh3cAAASlotSessionResourceNum": hh3cAAASlotSessionResourceNum}
)
