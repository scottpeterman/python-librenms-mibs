# SNMP MIB module (CISCOSB-RLINVENTORYENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-RLINVENTORYENT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:29:40 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class UnitIfindexType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unit", 0),
          ("ifindex", 1))
    )



# MIB Managed Objects in the order of their OIDs

_RlInventoryEntTable_Object = MibTable
rlInventoryEntTable = _RlInventoryEntTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217)
)
if mibBuilder.loadTexts:
    rlInventoryEntTable.setStatus("current")
_RlInventoryEntEntry_Object = MibTableRow
rlInventoryEntEntry = _RlInventoryEntEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1)
)
rlInventoryEntEntry.setIndexNames(
    (0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitOrIfindex"),
    (0, "CISCOSB-RLINVENTORYENT-MIB", "rlInventoryEntUnitIfindexID"),
)
if mibBuilder.loadTexts:
    rlInventoryEntEntry.setStatus("current")
_RlInventoryEntUnitOrIfindex_Type = UnitIfindexType
_RlInventoryEntUnitOrIfindex_Object = MibTableColumn
rlInventoryEntUnitOrIfindex = _RlInventoryEntUnitOrIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 1),
    _RlInventoryEntUnitOrIfindex_Type()
)
rlInventoryEntUnitOrIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntUnitOrIfindex.setStatus("current")
_RlInventoryEntUnitIfindexID_Type = Unsigned32
_RlInventoryEntUnitIfindexID_Object = MibTableColumn
rlInventoryEntUnitIfindexID = _RlInventoryEntUnitIfindexID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 2),
    _RlInventoryEntUnitIfindexID_Type()
)
rlInventoryEntUnitIfindexID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntUnitIfindexID.setStatus("current")
_RlInventoryEntVendorID_Type = DisplayString
_RlInventoryEntVendorID_Object = MibTableColumn
rlInventoryEntVendorID = _RlInventoryEntVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 3),
    _RlInventoryEntVendorID_Type()
)
rlInventoryEntVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntVendorID.setStatus("current")
_RlInventoryEntPID_Type = DisplayString
_RlInventoryEntPID_Object = MibTableColumn
rlInventoryEntPID = _RlInventoryEntPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 4),
    _RlInventoryEntPID_Type()
)
rlInventoryEntPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntPID.setStatus("current")
_RlInventoryEntName_Type = DisplayString
_RlInventoryEntName_Object = MibTableColumn
rlInventoryEntName = _RlInventoryEntName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 5),
    _RlInventoryEntName_Type()
)
rlInventoryEntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntName.setStatus("current")
_RlInventoryEntDescription_Type = DisplayString
_RlInventoryEntDescription_Object = MibTableColumn
rlInventoryEntDescription = _RlInventoryEntDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 6),
    _RlInventoryEntDescription_Type()
)
rlInventoryEntDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntDescription.setStatus("current")
_RlInventoryEntSerialNumber_Type = DisplayString
_RlInventoryEntSerialNumber_Object = MibTableColumn
rlInventoryEntSerialNumber = _RlInventoryEntSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 7),
    _RlInventoryEntSerialNumber_Type()
)
rlInventoryEntSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntSerialNumber.setStatus("current")
_RlInventoryEntUnitNum_Type = Unsigned32
_RlInventoryEntUnitNum_Object = MibTableColumn
rlInventoryEntUnitNum = _RlInventoryEntUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 217, 1, 8),
    _RlInventoryEntUnitNum_Type()
)
rlInventoryEntUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInventoryEntUnitNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-RLINVENTORYENT-MIB",
    **{"UnitIfindexType": UnitIfindexType,
       "rlInventoryEntTable": rlInventoryEntTable,
       "rlInventoryEntEntry": rlInventoryEntEntry,
       "rlInventoryEntUnitOrIfindex": rlInventoryEntUnitOrIfindex,
       "rlInventoryEntUnitIfindexID": rlInventoryEntUnitIfindexID,
       "rlInventoryEntVendorID": rlInventoryEntVendorID,
       "rlInventoryEntPID": rlInventoryEntPID,
       "rlInventoryEntName": rlInventoryEntName,
       "rlInventoryEntDescription": rlInventoryEntDescription,
       "rlInventoryEntSerialNumber": rlInventoryEntSerialNumber,
       "rlInventoryEntUnitNum": rlInventoryEntUnitNum}
)
