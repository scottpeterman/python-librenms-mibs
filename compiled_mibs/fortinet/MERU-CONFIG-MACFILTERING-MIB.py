# SNMP MIB module (MERU-CONFIG-MACFILTERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fortinet\MERU-CONFIG-MACFILTERING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:45:04 2025
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigMacFiltering = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwAcl_ObjectIdentity = ObjectIdentity
mwAcl = _MwAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 1)
)
_MwAclCachingTimeout_Type = Unsigned32
_MwAclCachingTimeout_Object = MibScalar
mwAclCachingTimeout = _MwAclCachingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 1, 4),
    _MwAclCachingTimeout_Type()
)
mwAclCachingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwAclCachingTimeout.setStatus("current")
_MwAclAccessAllowTable_Object = MibTable
mwAclAccessAllowTable = _MwAclAccessAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2)
)
if mibBuilder.loadTexts:
    mwAclAccessAllowTable.setStatus("current")
_MwAclAccessAllowEntry_Object = MibTableRow
mwAclAccessAllowEntry = _MwAclAccessAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1)
)
mwAclAccessAllowEntry.setIndexNames(
    (0, "MERU-CONFIG-MACFILTERING-MIB", "mwAclAccessAllowTableIndex"),
)
if mibBuilder.loadTexts:
    mwAclAccessAllowEntry.setStatus("current")
_MwAclAccessAllowTableIndex_Type = Integer32
_MwAclAccessAllowTableIndex_Object = MibTableColumn
mwAclAccessAllowTableIndex = _MwAclAccessAllowTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 1),
    _MwAclAccessAllowTableIndex_Type()
)
mwAclAccessAllowTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAclAccessAllowTableIndex.setStatus("current")
_MwAclAccessAllowMac_Type = MacAddress
_MwAclAccessAllowMac_Object = MibTableColumn
mwAclAccessAllowMac = _MwAclAccessAllowMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 2),
    _MwAclAccessAllowMac_Type()
)
mwAclAccessAllowMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessAllowMac.setStatus("current")


class _MwAclAccessAllowDescr_Type(DisplayString):
    """Custom type mwAclAccessAllowDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MwAclAccessAllowDescr_Type.__name__ = "DisplayString"
_MwAclAccessAllowDescr_Object = MibTableColumn
mwAclAccessAllowDescr = _MwAclAccessAllowDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 3),
    _MwAclAccessAllowDescr_Type()
)
mwAclAccessAllowDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessAllowDescr.setStatus("current")
_MwAclAccessAllowRowStatus_Type = RowStatus
_MwAclAccessAllowRowStatus_Object = MibTableColumn
mwAclAccessAllowRowStatus = _MwAclAccessAllowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 2, 1, 5),
    _MwAclAccessAllowRowStatus_Type()
)
mwAclAccessAllowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessAllowRowStatus.setStatus("current")
_MwAclAccessDenyTable_Object = MibTable
mwAclAccessDenyTable = _MwAclAccessDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3)
)
if mibBuilder.loadTexts:
    mwAclAccessDenyTable.setStatus("current")
_MwAclAccessDenyEntry_Object = MibTableRow
mwAclAccessDenyEntry = _MwAclAccessDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1)
)
mwAclAccessDenyEntry.setIndexNames(
    (0, "MERU-CONFIG-MACFILTERING-MIB", "mwAclAccessDenyTableIndex"),
)
if mibBuilder.loadTexts:
    mwAclAccessDenyEntry.setStatus("current")
_MwAclAccessDenyTableIndex_Type = Integer32
_MwAclAccessDenyTableIndex_Object = MibTableColumn
mwAclAccessDenyTableIndex = _MwAclAccessDenyTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 1),
    _MwAclAccessDenyTableIndex_Type()
)
mwAclAccessDenyTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAclAccessDenyTableIndex.setStatus("current")
_MwAclAccessDenyMac_Type = MacAddress
_MwAclAccessDenyMac_Object = MibTableColumn
mwAclAccessDenyMac = _MwAclAccessDenyMac_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 2),
    _MwAclAccessDenyMac_Type()
)
mwAclAccessDenyMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessDenyMac.setStatus("current")


class _MwAclAccessDenyDescr_Type(DisplayString):
    """Custom type mwAclAccessDenyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MwAclAccessDenyDescr_Type.__name__ = "DisplayString"
_MwAclAccessDenyDescr_Object = MibTableColumn
mwAclAccessDenyDescr = _MwAclAccessDenyDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 3),
    _MwAclAccessDenyDescr_Type()
)
mwAclAccessDenyDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessDenyDescr.setStatus("current")
_MwAclAccessDenyRowStatus_Type = RowStatus
_MwAclAccessDenyRowStatus_Object = MibTableColumn
mwAclAccessDenyRowStatus = _MwAclAccessDenyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 6, 3, 1, 5),
    _MwAclAccessDenyRowStatus_Type()
)
mwAclAccessDenyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAclAccessDenyRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-MACFILTERING-MIB",
    **{"mwConfigMacFiltering": mwConfigMacFiltering,
       "mwAcl": mwAcl,
       "mwAclCachingTimeout": mwAclCachingTimeout,
       "mwAclAccessAllowTable": mwAclAccessAllowTable,
       "mwAclAccessAllowEntry": mwAclAccessAllowEntry,
       "mwAclAccessAllowTableIndex": mwAclAccessAllowTableIndex,
       "mwAclAccessAllowMac": mwAclAccessAllowMac,
       "mwAclAccessAllowDescr": mwAclAccessAllowDescr,
       "mwAclAccessAllowRowStatus": mwAclAccessAllowRowStatus,
       "mwAclAccessDenyTable": mwAclAccessDenyTable,
       "mwAclAccessDenyEntry": mwAclAccessDenyEntry,
       "mwAclAccessDenyTableIndex": mwAclAccessDenyTableIndex,
       "mwAclAccessDenyMac": mwAclAccessDenyMac,
       "mwAclAccessDenyDescr": mwAclAccessDenyDescr,
       "mwAclAccessDenyRowStatus": mwAclAccessDenyRowStatus}
)
