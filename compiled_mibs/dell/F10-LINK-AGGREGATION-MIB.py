# SNMP MIB module (F10-LINK-AGGREGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dell\F10-LINK-AGGREGATION-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:05 2025
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(PortList,) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "PortList")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

f10LinkAggMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2)
)
if mibBuilder.loadTexts:
    f10LinkAggMib.setRevisions(
        ("1903-08-01 00:00",
         "1903-08-01 00:00",
         "1902-03-12 00:00",
         "1900-11-21 00:00",
         "1901-03-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10LinkAggObjects_ObjectIdentity = ObjectIdentity
f10LinkAggObjects = _F10LinkAggObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1)
)
_F10dot3dAgg_ObjectIdentity = ObjectIdentity
f10dot3dAgg = _F10dot3dAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1)
)
_Dot3aAggConfigTable_Object = MibTable
dot3aAggConfigTable = _Dot3aAggConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3aAggConfigTable.setStatus("current")
_Dot3aAggConfigEntry_Object = MibTableRow
dot3aAggConfigEntry = _Dot3aAggConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1)
)
dot3aAggConfigEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggCfgId"),
)
if mibBuilder.loadTexts:
    dot3aAggConfigEntry.setStatus("current")
_Dot3aAggCfgId_Type = Integer32
_Dot3aAggCfgId_Object = MibTableColumn
dot3aAggCfgId = _Dot3aAggCfgId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 1),
    _Dot3aAggCfgId_Type()
)
dot3aAggCfgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgId.setStatus("current")
_Dot3aAggCfgMacAddr_Type = MacAddress
_Dot3aAggCfgMacAddr_Object = MibTableColumn
dot3aAggCfgMacAddr = _Dot3aAggCfgMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 2),
    _Dot3aAggCfgMacAddr_Type()
)
dot3aAggCfgMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgMacAddr.setStatus("current")
_Dot3aAggCfgIfIndex_Type = Integer32
_Dot3aAggCfgIfIndex_Object = MibTableColumn
dot3aAggCfgIfIndex = _Dot3aAggCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 3),
    _Dot3aAggCfgIfIndex_Type()
)
dot3aAggCfgIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgIfIndex.setStatus("current")
_Dot3aAggCfgNumPorts_Type = Integer32
_Dot3aAggCfgNumPorts_Object = MibTableColumn
dot3aAggCfgNumPorts = _Dot3aAggCfgNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 4),
    _Dot3aAggCfgNumPorts_Type()
)
dot3aAggCfgNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgNumPorts.setStatus("current")
_Dot3aAggCfgPortList_Type = PortList
_Dot3aAggCfgPortList_Object = MibTableColumn
dot3aAggCfgPortList = _Dot3aAggCfgPortList_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 5),
    _Dot3aAggCfgPortList_Type()
)
dot3aAggCfgPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgPortList.setStatus("current")
_Dot3aAggCfgPortListString_Type = OctetString
_Dot3aAggCfgPortListString_Object = MibTableColumn
dot3aAggCfgPortListString = _Dot3aAggCfgPortListString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 1, 1, 6),
    _Dot3aAggCfgPortListString_Type()
)
dot3aAggCfgPortListString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggCfgPortListString.setStatus("deprecated")
_Dot3aAggStaticTable_Object = MibTable
dot3aAggStaticTable = _Dot3aAggStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot3aAggStaticTable.setStatus("current")
_Dot3aAggStaticEntry_Object = MibTableRow
dot3aAggStaticEntry = _Dot3aAggStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1)
)
dot3aAggStaticEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggIndex"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggMacAddr"),
)
if mibBuilder.loadTexts:
    dot3aAggStaticEntry.setStatus("deprecated")
_Dot3aAggIndex_Type = Integer32
_Dot3aAggIndex_Object = MibTableColumn
dot3aAggIndex = _Dot3aAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 1),
    _Dot3aAggIndex_Type()
)
dot3aAggIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggIndex.setStatus("deprecated")
_Dot3aAggVlanId_Type = Integer32
_Dot3aAggVlanId_Object = MibTableColumn
dot3aAggVlanId = _Dot3aAggVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 2),
    _Dot3aAggVlanId_Type()
)
dot3aAggVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggVlanId.setStatus("deprecated")
_Dot3aAggMacAddr_Type = MacAddress
_Dot3aAggMacAddr_Object = MibTableColumn
dot3aAggMacAddr = _Dot3aAggMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 3),
    _Dot3aAggMacAddr_Type()
)
dot3aAggMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggMacAddr.setStatus("deprecated")


class _Dot3aAggStatus_Type(Integer32):
    """Custom type dot3aAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aAggStatus_Type.__name__ = "Integer32"
_Dot3aAggStatus_Object = MibTableColumn
dot3aAggStatus = _Dot3aAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 4),
    _Dot3aAggStatus_Type()
)
dot3aAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggStatus.setStatus("deprecated")
_Dot3aAggDistributedPort_Type = OctetString
_Dot3aAggDistributedPort_Object = MibTableColumn
dot3aAggDistributedPort = _Dot3aAggDistributedPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 2, 1, 5),
    _Dot3aAggDistributedPort_Type()
)
dot3aAggDistributedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggDistributedPort.setStatus("deprecated")
_Dot3aAggFdbTable_Object = MibTable
dot3aAggFdbTable = _Dot3aAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dot3aAggFdbTable.setStatus("current")
_Dot3aAggFdbEntry_Object = MibTableRow
dot3aAggFdbEntry = _Dot3aAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1)
)
dot3aAggFdbEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggFdbIndex"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggFdbVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aAggFdbMacAddr"),
)
if mibBuilder.loadTexts:
    dot3aAggFdbEntry.setStatus("deprecated")
_Dot3aAggFdbIndex_Type = Integer32
_Dot3aAggFdbIndex_Object = MibTableColumn
dot3aAggFdbIndex = _Dot3aAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 1),
    _Dot3aAggFdbIndex_Type()
)
dot3aAggFdbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbIndex.setStatus("deprecated")
_Dot3aAggFdbVlanId_Type = Integer32
_Dot3aAggFdbVlanId_Object = MibTableColumn
dot3aAggFdbVlanId = _Dot3aAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 2),
    _Dot3aAggFdbVlanId_Type()
)
dot3aAggFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbVlanId.setStatus("deprecated")
_Dot3aAggFdbMacAddr_Type = MacAddress
_Dot3aAggFdbMacAddr_Object = MibTableColumn
dot3aAggFdbMacAddr = _Dot3aAggFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 3),
    _Dot3aAggFdbMacAddr_Type()
)
dot3aAggFdbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbMacAddr.setStatus("deprecated")


class _Dot3aAggFdbStatus_Type(Integer32):
    """Custom type dot3aAggFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aAggFdbStatus_Object = MibTableColumn
dot3aAggFdbStatus = _Dot3aAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 4),
    _Dot3aAggFdbStatus_Type()
)
dot3aAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbStatus.setStatus("deprecated")
_Dot3aAggFdbDistributedPort_Type = OctetString
_Dot3aAggFdbDistributedPort_Object = MibTableColumn
dot3aAggFdbDistributedPort = _Dot3aAggFdbDistributedPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 3, 1, 5),
    _Dot3aAggFdbDistributedPort_Type()
)
dot3aAggFdbDistributedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aAggFdbDistributedPort.setStatus("deprecated")
_Dot3aCurAggStaticTable_Object = MibTable
dot3aCurAggStaticTable = _Dot3aCurAggStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dot3aCurAggStaticTable.setStatus("current")
_Dot3aCurAggStaticEntry_Object = MibTableRow
dot3aCurAggStaticEntry = _Dot3aCurAggStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1)
)
dot3aCurAggStaticEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggMacAddr"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggIndex"),
)
if mibBuilder.loadTexts:
    dot3aCurAggStaticEntry.setStatus("current")
_Dot3aCurAggVlanId_Type = Integer32
_Dot3aCurAggVlanId_Object = MibTableColumn
dot3aCurAggVlanId = _Dot3aCurAggVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 1),
    _Dot3aCurAggVlanId_Type()
)
dot3aCurAggVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggVlanId.setStatus("current")
_Dot3aCurAggMacAddr_Type = MacAddress
_Dot3aCurAggMacAddr_Object = MibTableColumn
dot3aCurAggMacAddr = _Dot3aCurAggMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 2),
    _Dot3aCurAggMacAddr_Type()
)
dot3aCurAggMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggMacAddr.setStatus("current")
_Dot3aCurAggIndex_Type = Integer32
_Dot3aCurAggIndex_Object = MibTableColumn
dot3aCurAggIndex = _Dot3aCurAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 3),
    _Dot3aCurAggIndex_Type()
)
dot3aCurAggIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggIndex.setStatus("current")


class _Dot3aCurAggStatus_Type(Integer32):
    """Custom type dot3aCurAggStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aCurAggStatus_Type.__name__ = "Integer32"
_Dot3aCurAggStatus_Object = MibTableColumn
dot3aCurAggStatus = _Dot3aCurAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 4, 1, 4),
    _Dot3aCurAggStatus_Type()
)
dot3aCurAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggStatus.setStatus("current")
_Dot3aCurAggFdbTable_Object = MibTable
dot3aCurAggFdbTable = _Dot3aCurAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dot3aCurAggFdbTable.setStatus("current")
_Dot3aCurAggFdbEntry_Object = MibTableRow
dot3aCurAggFdbEntry = _Dot3aCurAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1)
)
dot3aCurAggFdbEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbVlanId"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbMacAddr"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbIndex"),
)
if mibBuilder.loadTexts:
    dot3aCurAggFdbEntry.setStatus("current")
_Dot3aCurAggFdbVlanId_Type = Integer32
_Dot3aCurAggFdbVlanId_Object = MibTableColumn
dot3aCurAggFdbVlanId = _Dot3aCurAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 1),
    _Dot3aCurAggFdbVlanId_Type()
)
dot3aCurAggFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggFdbVlanId.setStatus("current")
_Dot3aCurAggFdbMacAddr_Type = MacAddress
_Dot3aCurAggFdbMacAddr_Object = MibTableColumn
dot3aCurAggFdbMacAddr = _Dot3aCurAggFdbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 2),
    _Dot3aCurAggFdbMacAddr_Type()
)
dot3aCurAggFdbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggFdbMacAddr.setStatus("current")
_Dot3aCurAggFdbIndex_Type = Integer32
_Dot3aCurAggFdbIndex_Object = MibTableColumn
dot3aCurAggFdbIndex = _Dot3aCurAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 3),
    _Dot3aCurAggFdbIndex_Type()
)
dot3aCurAggFdbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggFdbIndex.setStatus("current")


class _Dot3aCurAggFdbStatus_Type(Integer32):
    """Custom type dot3aCurAggFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aCurAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aCurAggFdbStatus_Object = MibTableColumn
dot3aCurAggFdbStatus = _Dot3aCurAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 5, 1, 4),
    _Dot3aCurAggFdbStatus_Type()
)
dot3aCurAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCurAggFdbStatus.setStatus("current")
_Dot3aCommonAggFdbTable_Object = MibTable
dot3aCommonAggFdbTable = _Dot3aCommonAggFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dot3aCommonAggFdbTable.setStatus("current")
_Dot3aCommonAggFdbEntry_Object = MibTableRow
dot3aCommonAggFdbEntry = _Dot3aCommonAggFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1)
)
dot3aCommonAggFdbEntry.setIndexNames(
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbIndex"),
    (0, "F10-LINK-AGGREGATION-MIB", "dot3aCommonAggFdbVlanId"),
)
if mibBuilder.loadTexts:
    dot3aCommonAggFdbEntry.setStatus("current")
_Dot3aCommonAggFdbIndex_Type = Integer32
_Dot3aCommonAggFdbIndex_Object = MibTableColumn
dot3aCommonAggFdbIndex = _Dot3aCommonAggFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 1),
    _Dot3aCommonAggFdbIndex_Type()
)
dot3aCommonAggFdbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbIndex.setStatus("current")
_Dot3aCommonAggFdbVlanId_Type = Integer32
_Dot3aCommonAggFdbVlanId_Object = MibTableColumn
dot3aCommonAggFdbVlanId = _Dot3aCommonAggFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 2),
    _Dot3aCommonAggFdbVlanId_Type()
)
dot3aCommonAggFdbVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbVlanId.setStatus("current")


class _Dot3aCommonAggFdbTagConfig_Type(Integer32):
    """Custom type dot3aCommonAggFdbTagConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_Dot3aCommonAggFdbTagConfig_Type.__name__ = "Integer32"
_Dot3aCommonAggFdbTagConfig_Object = MibTableColumn
dot3aCommonAggFdbTagConfig = _Dot3aCommonAggFdbTagConfig_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 3),
    _Dot3aCommonAggFdbTagConfig_Type()
)
dot3aCommonAggFdbTagConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbTagConfig.setStatus("current")


class _Dot3aCommonAggFdbStatus_Type(Integer32):
    """Custom type dot3aCommonAggFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Dot3aCommonAggFdbStatus_Type.__name__ = "Integer32"
_Dot3aCommonAggFdbStatus_Object = MibTableColumn
dot3aCommonAggFdbStatus = _Dot3aCommonAggFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 1, 6, 1, 4),
    _Dot3aCommonAggFdbStatus_Type()
)
dot3aCommonAggFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3aCommonAggFdbStatus.setStatus("current")
_F10LinkAggMgmt_ObjectIdentity = ObjectIdentity
f10LinkAggMgmt = _F10LinkAggMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 2)
)


class _Dot3aClearFdb_Type(Integer32):
    """Custom type dot3aClearFdb based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_Dot3aClearFdb_Type.__name__ = "Integer32"
_Dot3aClearFdb_Object = MibScalar
dot3aClearFdb = _Dot3aClearFdb_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 1, 2, 1),
    _Dot3aClearFdb_Type()
)
dot3aClearFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3aClearFdb.setStatus("current")
_F10LinkAggMibConformance_ObjectIdentity = ObjectIdentity
f10LinkAggMibConformance = _F10LinkAggMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2)
)
_F10LinkAggMibCompliances_ObjectIdentity = ObjectIdentity
f10LinkAggMibCompliances = _F10LinkAggMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1)
)
_F10LinkAggMibGroups_ObjectIdentity = ObjectIdentity
f10LinkAggMibGroups = _F10LinkAggMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 2)
)

# Managed Objects groups

f10CommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 2, 1)
)
f10CommonGroup.setObjects(
      *(("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgMacAddr"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgIfIndex"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgNumPorts"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggCfgPortList"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggDistributedPort"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggFdbStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aAggFdbDistributedPort"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCurAggStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aCurAggFdbStatus"),
        ("F10-LINK-AGGREGATION-MIB", "dot3aClearFdb"))
)
if mibBuilder.loadTexts:
    f10CommonGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f10LinkAggMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 2, 2, 1, 1)
)
f10LinkAggMibCompliance.setObjects(
    ("F10-LINK-AGGREGATION-MIB", "f10CommonGroup")
)
if mibBuilder.loadTexts:
    f10LinkAggMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-LINK-AGGREGATION-MIB",
    **{"f10LinkAggMib": f10LinkAggMib,
       "f10LinkAggObjects": f10LinkAggObjects,
       "f10dot3dAgg": f10dot3dAgg,
       "dot3aAggConfigTable": dot3aAggConfigTable,
       "dot3aAggConfigEntry": dot3aAggConfigEntry,
       "dot3aAggCfgId": dot3aAggCfgId,
       "dot3aAggCfgMacAddr": dot3aAggCfgMacAddr,
       "dot3aAggCfgIfIndex": dot3aAggCfgIfIndex,
       "dot3aAggCfgNumPorts": dot3aAggCfgNumPorts,
       "dot3aAggCfgPortList": dot3aAggCfgPortList,
       "dot3aAggCfgPortListString": dot3aAggCfgPortListString,
       "dot3aAggStaticTable": dot3aAggStaticTable,
       "dot3aAggStaticEntry": dot3aAggStaticEntry,
       "dot3aAggIndex": dot3aAggIndex,
       "dot3aAggVlanId": dot3aAggVlanId,
       "dot3aAggMacAddr": dot3aAggMacAddr,
       "dot3aAggStatus": dot3aAggStatus,
       "dot3aAggDistributedPort": dot3aAggDistributedPort,
       "dot3aAggFdbTable": dot3aAggFdbTable,
       "dot3aAggFdbEntry": dot3aAggFdbEntry,
       "dot3aAggFdbIndex": dot3aAggFdbIndex,
       "dot3aAggFdbVlanId": dot3aAggFdbVlanId,
       "dot3aAggFdbMacAddr": dot3aAggFdbMacAddr,
       "dot3aAggFdbStatus": dot3aAggFdbStatus,
       "dot3aAggFdbDistributedPort": dot3aAggFdbDistributedPort,
       "dot3aCurAggStaticTable": dot3aCurAggStaticTable,
       "dot3aCurAggStaticEntry": dot3aCurAggStaticEntry,
       "dot3aCurAggVlanId": dot3aCurAggVlanId,
       "dot3aCurAggMacAddr": dot3aCurAggMacAddr,
       "dot3aCurAggIndex": dot3aCurAggIndex,
       "dot3aCurAggStatus": dot3aCurAggStatus,
       "dot3aCurAggFdbTable": dot3aCurAggFdbTable,
       "dot3aCurAggFdbEntry": dot3aCurAggFdbEntry,
       "dot3aCurAggFdbVlanId": dot3aCurAggFdbVlanId,
       "dot3aCurAggFdbMacAddr": dot3aCurAggFdbMacAddr,
       "dot3aCurAggFdbIndex": dot3aCurAggFdbIndex,
       "dot3aCurAggFdbStatus": dot3aCurAggFdbStatus,
       "dot3aCommonAggFdbTable": dot3aCommonAggFdbTable,
       "dot3aCommonAggFdbEntry": dot3aCommonAggFdbEntry,
       "dot3aCommonAggFdbIndex": dot3aCommonAggFdbIndex,
       "dot3aCommonAggFdbVlanId": dot3aCommonAggFdbVlanId,
       "dot3aCommonAggFdbTagConfig": dot3aCommonAggFdbTagConfig,
       "dot3aCommonAggFdbStatus": dot3aCommonAggFdbStatus,
       "f10LinkAggMgmt": f10LinkAggMgmt,
       "dot3aClearFdb": dot3aClearFdb,
       "f10LinkAggMibConformance": f10LinkAggMibConformance,
       "f10LinkAggMibCompliances": f10LinkAggMibCompliances,
       "f10LinkAggMibCompliance": f10LinkAggMibCompliance,
       "f10LinkAggMibGroups": f10LinkAggMibGroups,
       "f10CommonGroup": f10CommonGroup}
)
