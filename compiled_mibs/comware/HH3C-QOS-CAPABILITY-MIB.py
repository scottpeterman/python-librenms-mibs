# SNMP MIB module (HH3C-QOS-CAPABILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-QOS-CAPABILITY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:32:37 2025
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

(hh3cSNMPAgCpb,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cSNMPAgCpb")

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

hh3cQosCapability = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cQosCapability.setRevisions(
        ("2016-10-25 00:00",
         "2014-10-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CapabilityPhysicalType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("stack", 1),
          ("chassis", 2),
          ("module", 3),
          ("port", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hh3cQoSCapabilityMibObjects_ObjectIdentity = ObjectIdentity
hh3cQoSCapabilityMibObjects = _Hh3cQoSCapabilityMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1)
)
_Hh3cQoSCapabilityGroup_ObjectIdentity = ObjectIdentity
hh3cQoSCapabilityGroup = _Hh3cQoSCapabilityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1)
)
_Hh3cQoSCapabilityTable_Object = MibTable
hh3cQoSCapabilityTable = _Hh3cQoSCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cQoSCapabilityTable.setStatus("current")
_Hh3cQoSCapabilityEntry_Object = MibTableRow
hh3cQoSCapabilityEntry = _Hh3cQoSCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1)
)
hh3cQoSCapabilityEntry.setIndexNames(
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCapabilityPhysicalType"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCapabilityPhysicalIndex"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSModuleIndex"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSCapabilityEntry.setStatus("current")
_Hh3cQoSCapabilityPhysicalType_Type = CapabilityPhysicalType
_Hh3cQoSCapabilityPhysicalType_Object = MibTableColumn
hh3cQoSCapabilityPhysicalType = _Hh3cQoSCapabilityPhysicalType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 1),
    _Hh3cQoSCapabilityPhysicalType_Type()
)
hh3cQoSCapabilityPhysicalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSCapabilityPhysicalType.setStatus("current")
_Hh3cQoSCapabilityPhysicalIndex_Type = Integer32
_Hh3cQoSCapabilityPhysicalIndex_Object = MibTableColumn
hh3cQoSCapabilityPhysicalIndex = _Hh3cQoSCapabilityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 2),
    _Hh3cQoSCapabilityPhysicalIndex_Type()
)
hh3cQoSCapabilityPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSCapabilityPhysicalIndex.setStatus("current")
_Hh3cQoSModuleIndex_Type = Integer32
_Hh3cQoSModuleIndex_Object = MibTableColumn
hh3cQoSModuleIndex = _Hh3cQoSModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 3),
    _Hh3cQoSModuleIndex_Type()
)
hh3cQoSModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSModuleIndex.setStatus("current")
_Hh3cQoSCharacteristicsIndex_Type = Integer32
_Hh3cQoSCharacteristicsIndex_Object = MibTableColumn
hh3cQoSCharacteristicsIndex = _Hh3cQoSCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 4),
    _Hh3cQoSCharacteristicsIndex_Type()
)
hh3cQoSCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSCharacteristicsIndex.setStatus("current")
_Hh3cQoSCharacteristicsValue_Type = Unsigned32
_Hh3cQoSCharacteristicsValue_Object = MibTableColumn
hh3cQoSCharacteristicsValue = _Hh3cQoSCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 1, 1, 5),
    _Hh3cQoSCharacteristicsValue_Type()
)
hh3cQoSCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSCharacteristicsValue.setStatus("current")
_Hh3cQoSSysCapabilityTable_Object = MibTable
hh3cQoSSysCapabilityTable = _Hh3cQoSSysCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cQoSSysCapabilityTable.setStatus("current")
_Hh3cQoSSysCapabilityEntry_Object = MibTableRow
hh3cQoSSysCapabilityEntry = _Hh3cQoSSysCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 2, 1)
)
hh3cQoSSysCapabilityEntry.setIndexNames(
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSSysCapModuleIndex"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSSysCapCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSSysCapabilityEntry.setStatus("current")


class _Hh3cQoSSysCapModuleIndex_Type(Integer32):
    """Custom type hh3cQoSSysCapModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cQoSSysCapModuleIndex_Type.__name__ = "Integer32"
_Hh3cQoSSysCapModuleIndex_Object = MibTableColumn
hh3cQoSSysCapModuleIndex = _Hh3cQoSSysCapModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 2, 1, 1),
    _Hh3cQoSSysCapModuleIndex_Type()
)
hh3cQoSSysCapModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSSysCapModuleIndex.setStatus("current")


class _Hh3cQoSSysCapCharacteristicsIndex_Type(Integer32):
    """Custom type hh3cQoSSysCapCharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cQoSSysCapCharacteristicsIndex_Type.__name__ = "Integer32"
_Hh3cQoSSysCapCharacteristicsIndex_Object = MibTableColumn
hh3cQoSSysCapCharacteristicsIndex = _Hh3cQoSSysCapCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 2, 1, 2),
    _Hh3cQoSSysCapCharacteristicsIndex_Type()
)
hh3cQoSSysCapCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSSysCapCharacteristicsIndex.setStatus("current")
_Hh3cQoSSysCapCharacteristicsValue_Type = Unsigned32
_Hh3cQoSSysCapCharacteristicsValue_Object = MibTableColumn
hh3cQoSSysCapCharacteristicsValue = _Hh3cQoSSysCapCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 2, 1, 3),
    _Hh3cQoSSysCapCharacteristicsValue_Type()
)
hh3cQoSSysCapCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSSysCapCharacteristicsValue.setStatus("current")
_Hh3cQoSIfCapabilityTable_Object = MibTable
hh3cQoSIfCapabilityTable = _Hh3cQoSIfCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cQoSIfCapabilityTable.setStatus("current")
_Hh3cQoSIfCapabilityEntry_Object = MibTableRow
hh3cQoSIfCapabilityEntry = _Hh3cQoSIfCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 3, 1)
)
hh3cQoSIfCapabilityEntry.setIndexNames(
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSIfCapIfIndex"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSIfCapModuleIndex"),
    (0, "HH3C-QOS-CAPABILITY-MIB", "hh3cQoSIfCapCharacteristicsIndex"),
)
if mibBuilder.loadTexts:
    hh3cQoSIfCapabilityEntry.setStatus("current")


class _Hh3cQoSIfCapIfIndex_Type(Integer32):
    """Custom type hh3cQoSIfCapIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cQoSIfCapIfIndex_Type.__name__ = "Integer32"
_Hh3cQoSIfCapIfIndex_Object = MibTableColumn
hh3cQoSIfCapIfIndex = _Hh3cQoSIfCapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 3, 1, 1),
    _Hh3cQoSIfCapIfIndex_Type()
)
hh3cQoSIfCapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSIfCapIfIndex.setStatus("current")


class _Hh3cQoSIfCapModuleIndex_Type(Integer32):
    """Custom type hh3cQoSIfCapModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cQoSIfCapModuleIndex_Type.__name__ = "Integer32"
_Hh3cQoSIfCapModuleIndex_Object = MibTableColumn
hh3cQoSIfCapModuleIndex = _Hh3cQoSIfCapModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 3, 1, 2),
    _Hh3cQoSIfCapModuleIndex_Type()
)
hh3cQoSIfCapModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSIfCapModuleIndex.setStatus("current")


class _Hh3cQoSIfCapCharacteristicsIndex_Type(Integer32):
    """Custom type hh3cQoSIfCapCharacteristicsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cQoSIfCapCharacteristicsIndex_Type.__name__ = "Integer32"
_Hh3cQoSIfCapCharacteristicsIndex_Object = MibTableColumn
hh3cQoSIfCapCharacteristicsIndex = _Hh3cQoSIfCapCharacteristicsIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 3, 1, 3),
    _Hh3cQoSIfCapCharacteristicsIndex_Type()
)
hh3cQoSIfCapCharacteristicsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cQoSIfCapCharacteristicsIndex.setStatus("current")
_Hh3cQoSIfCapCharacteristicsValue_Type = Unsigned32
_Hh3cQoSIfCapCharacteristicsValue_Object = MibTableColumn
hh3cQoSIfCapCharacteristicsValue = _Hh3cQoSIfCapCharacteristicsValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 7, 1, 1, 1, 3, 1, 4),
    _Hh3cQoSIfCapCharacteristicsValue_Type()
)
hh3cQoSIfCapCharacteristicsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQoSIfCapCharacteristicsValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-QOS-CAPABILITY-MIB",
    **{"CapabilityPhysicalType": CapabilityPhysicalType,
       "hh3cQosCapability": hh3cQosCapability,
       "hh3cQoSCapabilityMibObjects": hh3cQoSCapabilityMibObjects,
       "hh3cQoSCapabilityGroup": hh3cQoSCapabilityGroup,
       "hh3cQoSCapabilityTable": hh3cQoSCapabilityTable,
       "hh3cQoSCapabilityEntry": hh3cQoSCapabilityEntry,
       "hh3cQoSCapabilityPhysicalType": hh3cQoSCapabilityPhysicalType,
       "hh3cQoSCapabilityPhysicalIndex": hh3cQoSCapabilityPhysicalIndex,
       "hh3cQoSModuleIndex": hh3cQoSModuleIndex,
       "hh3cQoSCharacteristicsIndex": hh3cQoSCharacteristicsIndex,
       "hh3cQoSCharacteristicsValue": hh3cQoSCharacteristicsValue,
       "hh3cQoSSysCapabilityTable": hh3cQoSSysCapabilityTable,
       "hh3cQoSSysCapabilityEntry": hh3cQoSSysCapabilityEntry,
       "hh3cQoSSysCapModuleIndex": hh3cQoSSysCapModuleIndex,
       "hh3cQoSSysCapCharacteristicsIndex": hh3cQoSSysCapCharacteristicsIndex,
       "hh3cQoSSysCapCharacteristicsValue": hh3cQoSSysCapCharacteristicsValue,
       "hh3cQoSIfCapabilityTable": hh3cQoSIfCapabilityTable,
       "hh3cQoSIfCapabilityEntry": hh3cQoSIfCapabilityEntry,
       "hh3cQoSIfCapIfIndex": hh3cQoSIfCapIfIndex,
       "hh3cQoSIfCapModuleIndex": hh3cQoSIfCapModuleIndex,
       "hh3cQoSIfCapCharacteristicsIndex": hh3cQoSIfCapCharacteristicsIndex,
       "hh3cQoSIfCapCharacteristicsValue": hh3cQoSIfCapCharacteristicsValue}
)
