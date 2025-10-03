# SNMP MIB module (HH3C-RES-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-RES-MON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:43 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cResMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169)
)
if mibBuilder.loadTexts:
    hh3cResMon.setRevisions(
        ("2017-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cResMonScalarObjects_ObjectIdentity = ObjectIdentity
hh3cResMonScalarObjects = _Hh3cResMonScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 1)
)
_Hh3cResMonMinorResendEnable_Type = TruthValue
_Hh3cResMonMinorResendEnable_Object = MibScalar
hh3cResMonMinorResendEnable = _Hh3cResMonMinorResendEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 1, 1),
    _Hh3cResMonMinorResendEnable_Type()
)
hh3cResMonMinorResendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cResMonMinorResendEnable.setStatus("current")


class _Hh3cResMonOutputEnable_Type(Bits):
    """Custom type hh3cResMonOutputEnable based on Bits"""
    namedValues = NamedValues(
        *(("syslog", 0),
          ("snmpNotification", 1),
          ("netconfEvent", 2))
    )

_Hh3cResMonOutputEnable_Type.__name__ = "Bits"
_Hh3cResMonOutputEnable_Object = MibScalar
hh3cResMonOutputEnable = _Hh3cResMonOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 1, 2),
    _Hh3cResMonOutputEnable_Type()
)
hh3cResMonOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cResMonOutputEnable.setStatus("current")
_Hh3cResMonTables_ObjectIdentity = ObjectIdentity
hh3cResMonTables = _Hh3cResMonTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2)
)
_Hh3cResMonConfigTable_Object = MibTable
hh3cResMonConfigTable = _Hh3cResMonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cResMonConfigTable.setStatus("current")
_Hh3cResMonConfigEntry_Object = MibTableRow
hh3cResMonConfigEntry = _Hh3cResMonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1)
)
hh3cResMonConfigEntry.setIndexNames(
    (0, "HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
    (0, "HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
    (0, "HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
    (0, "HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
)
if mibBuilder.loadTexts:
    hh3cResMonConfigEntry.setStatus("current")
_Hh3cResMonChassisIndex_Type = Unsigned32
_Hh3cResMonChassisIndex_Object = MibTableColumn
hh3cResMonChassisIndex = _Hh3cResMonChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1, 1),
    _Hh3cResMonChassisIndex_Type()
)
hh3cResMonChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonChassisIndex.setStatus("current")
_Hh3cResMonSlotIndex_Type = Unsigned32
_Hh3cResMonSlotIndex_Object = MibTableColumn
hh3cResMonSlotIndex = _Hh3cResMonSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1, 2),
    _Hh3cResMonSlotIndex_Type()
)
hh3cResMonSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonSlotIndex.setStatus("current")
_Hh3cResMonCpuIndex_Type = Unsigned32
_Hh3cResMonCpuIndex_Object = MibTableColumn
hh3cResMonCpuIndex = _Hh3cResMonCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1, 3),
    _Hh3cResMonCpuIndex_Type()
)
hh3cResMonCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonCpuIndex.setStatus("current")


class _Hh3cResMonResourceName_Type(OctetString):
    """Custom type hh3cResMonResourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hh3cResMonResourceName_Type.__name__ = "OctetString"
_Hh3cResMonResourceName_Object = MibTableColumn
hh3cResMonResourceName = _Hh3cResMonResourceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1, 4),
    _Hh3cResMonResourceName_Type()
)
hh3cResMonResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonResourceName.setStatus("current")


class _Hh3cResMonThresholdUnit_Type(Integer32):
    """Custom type hh3cResMonThresholdUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percentage", 2))
    )


_Hh3cResMonThresholdUnit_Type.__name__ = "Integer32"
_Hh3cResMonThresholdUnit_Object = MibTableColumn
hh3cResMonThresholdUnit = _Hh3cResMonThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1, 5),
    _Hh3cResMonThresholdUnit_Type()
)
hh3cResMonThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cResMonThresholdUnit.setStatus("current")
_Hh3cResMonMinorThreshold_Type = Unsigned32
_Hh3cResMonMinorThreshold_Object = MibTableColumn
hh3cResMonMinorThreshold = _Hh3cResMonMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1, 6),
    _Hh3cResMonMinorThreshold_Type()
)
hh3cResMonMinorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cResMonMinorThreshold.setStatus("current")
_Hh3cResMonSevereThreshold_Type = Unsigned32
_Hh3cResMonSevereThreshold_Object = MibTableColumn
hh3cResMonSevereThreshold = _Hh3cResMonSevereThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 1, 1, 7),
    _Hh3cResMonSevereThreshold_Type()
)
hh3cResMonSevereThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cResMonSevereThreshold.setStatus("current")
_Hh3cResMonInfoTable_Object = MibTable
hh3cResMonInfoTable = _Hh3cResMonInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cResMonInfoTable.setStatus("current")
_Hh3cResMonInfoEntry_Object = MibTableRow
hh3cResMonInfoEntry = _Hh3cResMonInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 2, 1)
)
hh3cResMonInfoEntry.setIndexNames(
    (0, "HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
    (0, "HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
    (0, "HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
    (0, "HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
)
if mibBuilder.loadTexts:
    hh3cResMonInfoEntry.setStatus("current")


class _Hh3cResMonUnit_Type(Integer32):
    """Custom type hh3cResMonUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percentage", 2))
    )


_Hh3cResMonUnit_Type.__name__ = "Integer32"
_Hh3cResMonUnit_Object = MibTableColumn
hh3cResMonUnit = _Hh3cResMonUnit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 2, 1, 1),
    _Hh3cResMonUnit_Type()
)
hh3cResMonUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonUnit.setStatus("current")
_Hh3cResMonCurrent_Type = Unsigned32
_Hh3cResMonCurrent_Object = MibTableColumn
hh3cResMonCurrent = _Hh3cResMonCurrent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 2, 1, 2),
    _Hh3cResMonCurrent_Type()
)
hh3cResMonCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonCurrent.setStatus("current")
_Hh3cResMonFree_Type = Unsigned32
_Hh3cResMonFree_Object = MibTableColumn
hh3cResMonFree = _Hh3cResMonFree_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 2, 1, 3),
    _Hh3cResMonFree_Type()
)
hh3cResMonFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonFree.setStatus("current")
_Hh3cResMonTotal_Type = Unsigned32
_Hh3cResMonTotal_Object = MibTableColumn
hh3cResMonTotal = _Hh3cResMonTotal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 2, 2, 1, 4),
    _Hh3cResMonTotal_Type()
)
hh3cResMonTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cResMonTotal.setStatus("current")
_Hh3cResMonNotification_ObjectIdentity = ObjectIdentity
hh3cResMonNotification = _Hh3cResMonNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3)
)
_Hh3cResMonTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cResMonTrapPrefix = _Hh3cResMonTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 0)
)
_Hh3cResMonTrapInfor_ObjectIdentity = ObjectIdentity
hh3cResMonTrapInfor = _Hh3cResMonTrapInfor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 1)
)


class _Hh3cResMonAdditionalInfo_Type(OctetString):
    """Custom type hh3cResMonAdditionalInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cResMonAdditionalInfo_Type.__name__ = "OctetString"
_Hh3cResMonAdditionalInfo_Object = MibScalar
hh3cResMonAdditionalInfo = _Hh3cResMonAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 1, 1),
    _Hh3cResMonAdditionalInfo_Type()
)
hh3cResMonAdditionalInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cResMonAdditionalInfo.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cResMonMinorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 0, 1)
)
hh3cResMonMinorNotification.setObjects(
      *(("HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
        ("HH3C-RES-MON-MIB", "hh3cResMonThresholdUnit"),
        ("HH3C-RES-MON-MIB", "hh3cResMonMinorThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSevereThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCurrent"),
        ("HH3C-RES-MON-MIB", "hh3cResMonFree"),
        ("HH3C-RES-MON-MIB", "hh3cResMonTotal"),
        ("HH3C-RES-MON-MIB", "hh3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    hh3cResMonMinorNotification.setStatus(
        "current"
    )

hh3cResMonMinorRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 0, 2)
)
hh3cResMonMinorRecoverNotification.setObjects(
      *(("HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
        ("HH3C-RES-MON-MIB", "hh3cResMonThresholdUnit"),
        ("HH3C-RES-MON-MIB", "hh3cResMonMinorThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSevereThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCurrent"),
        ("HH3C-RES-MON-MIB", "hh3cResMonFree"),
        ("HH3C-RES-MON-MIB", "hh3cResMonTotal"),
        ("HH3C-RES-MON-MIB", "hh3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    hh3cResMonMinorRecoverNotification.setStatus(
        "current"
    )

hh3cResMonSevereNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 0, 3)
)
hh3cResMonSevereNotification.setObjects(
      *(("HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
        ("HH3C-RES-MON-MIB", "hh3cResMonThresholdUnit"),
        ("HH3C-RES-MON-MIB", "hh3cResMonMinorThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSevereThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCurrent"),
        ("HH3C-RES-MON-MIB", "hh3cResMonFree"),
        ("HH3C-RES-MON-MIB", "hh3cResMonTotal"),
        ("HH3C-RES-MON-MIB", "hh3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    hh3cResMonSevereNotification.setStatus(
        "current"
    )

hh3cResMonSevereRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 0, 4)
)
hh3cResMonSevereRecoverNotification.setObjects(
      *(("HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
        ("HH3C-RES-MON-MIB", "hh3cResMonThresholdUnit"),
        ("HH3C-RES-MON-MIB", "hh3cResMonMinorThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSevereThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCurrent"),
        ("HH3C-RES-MON-MIB", "hh3cResMonFree"),
        ("HH3C-RES-MON-MIB", "hh3cResMonTotal"),
        ("HH3C-RES-MON-MIB", "hh3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    hh3cResMonSevereRecoverNotification.setStatus(
        "current"
    )

hh3cResMonUsedUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 0, 5)
)
hh3cResMonUsedUpNotification.setObjects(
      *(("HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
        ("HH3C-RES-MON-MIB", "hh3cResMonThresholdUnit"),
        ("HH3C-RES-MON-MIB", "hh3cResMonMinorThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSevereThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCurrent"),
        ("HH3C-RES-MON-MIB", "hh3cResMonFree"),
        ("HH3C-RES-MON-MIB", "hh3cResMonTotal"),
        ("HH3C-RES-MON-MIB", "hh3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    hh3cResMonUsedUpNotification.setStatus(
        "current"
    )

hh3cResMonUsedUpRecoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 169, 3, 0, 6)
)
hh3cResMonUsedUpRecoverNotification.setObjects(
      *(("HH3C-RES-MON-MIB", "hh3cResMonChassisIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSlotIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCpuIndex"),
        ("HH3C-RES-MON-MIB", "hh3cResMonResourceName"),
        ("HH3C-RES-MON-MIB", "hh3cResMonThresholdUnit"),
        ("HH3C-RES-MON-MIB", "hh3cResMonMinorThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonSevereThreshold"),
        ("HH3C-RES-MON-MIB", "hh3cResMonCurrent"),
        ("HH3C-RES-MON-MIB", "hh3cResMonFree"),
        ("HH3C-RES-MON-MIB", "hh3cResMonTotal"),
        ("HH3C-RES-MON-MIB", "hh3cResMonAdditionalInfo"))
)
if mibBuilder.loadTexts:
    hh3cResMonUsedUpRecoverNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RES-MON-MIB",
    **{"hh3cResMon": hh3cResMon,
       "hh3cResMonScalarObjects": hh3cResMonScalarObjects,
       "hh3cResMonMinorResendEnable": hh3cResMonMinorResendEnable,
       "hh3cResMonOutputEnable": hh3cResMonOutputEnable,
       "hh3cResMonTables": hh3cResMonTables,
       "hh3cResMonConfigTable": hh3cResMonConfigTable,
       "hh3cResMonConfigEntry": hh3cResMonConfigEntry,
       "hh3cResMonChassisIndex": hh3cResMonChassisIndex,
       "hh3cResMonSlotIndex": hh3cResMonSlotIndex,
       "hh3cResMonCpuIndex": hh3cResMonCpuIndex,
       "hh3cResMonResourceName": hh3cResMonResourceName,
       "hh3cResMonThresholdUnit": hh3cResMonThresholdUnit,
       "hh3cResMonMinorThreshold": hh3cResMonMinorThreshold,
       "hh3cResMonSevereThreshold": hh3cResMonSevereThreshold,
       "hh3cResMonInfoTable": hh3cResMonInfoTable,
       "hh3cResMonInfoEntry": hh3cResMonInfoEntry,
       "hh3cResMonUnit": hh3cResMonUnit,
       "hh3cResMonCurrent": hh3cResMonCurrent,
       "hh3cResMonFree": hh3cResMonFree,
       "hh3cResMonTotal": hh3cResMonTotal,
       "hh3cResMonNotification": hh3cResMonNotification,
       "hh3cResMonTrapPrefix": hh3cResMonTrapPrefix,
       "hh3cResMonMinorNotification": hh3cResMonMinorNotification,
       "hh3cResMonMinorRecoverNotification": hh3cResMonMinorRecoverNotification,
       "hh3cResMonSevereNotification": hh3cResMonSevereNotification,
       "hh3cResMonSevereRecoverNotification": hh3cResMonSevereRecoverNotification,
       "hh3cResMonUsedUpNotification": hh3cResMonUsedUpNotification,
       "hh3cResMonUsedUpRecoverNotification": hh3cResMonUsedUpRecoverNotification,
       "hh3cResMonTrapInfor": hh3cResMonTrapInfor,
       "hh3cResMonAdditionalInfo": hh3cResMonAdditionalInfo}
)
