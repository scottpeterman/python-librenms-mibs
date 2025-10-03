# SNMP MIB module (WLSX-TUNNELEDNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos\WLSX-TUNNELEDNODE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:57 2025
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

(wlsxEnterpriseMibModules,) = mibBuilder.importSymbols(
    "ARUBA-MIB",
    "wlsxEnterpriseMibModules")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

wlsxTunneledNodeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17)
)
if mibBuilder.loadTexts:
    wlsxTunneledNodeMIB.setRevisions(
        ("2020-08-14 17:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WlsxTunneledNodeOpGroup_ObjectIdentity = ObjectIdentity
wlsxTunneledNodeOpGroup = _WlsxTunneledNodeOpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1)
)
_WlsxTunneledNodeRequestTable_Object = MibTable
wlsxTunneledNodeRequestTable = _WlsxTunneledNodeRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    wlsxTunneledNodeRequestTable.setStatus("current")
_WlsxTunneledNodeRequestEntry_Object = MibTableRow
wlsxTunneledNodeRequestEntry = _WlsxTunneledNodeRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1)
)
wlsxTunneledNodeRequestEntry.setIndexNames(
    (0, "WLSX-TUNNELEDNODE-MIB", "wlsxTunneledNodeMAC"),
)
if mibBuilder.loadTexts:
    wlsxTunneledNodeRequestEntry.setStatus("current")
_WlsxTunneledNodeMAC_Type = MacAddress
_WlsxTunneledNodeMAC_Object = MibTableColumn
wlsxTunneledNodeMAC = _WlsxTunneledNodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 1),
    _WlsxTunneledNodeMAC_Type()
)
wlsxTunneledNodeMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wlsxTunneledNodeMAC.setStatus("current")
_WlsxTunneledNodeIp_Type = IpAddress
_WlsxTunneledNodeIp_Object = MibTableColumn
wlsxTunneledNodeIp = _WlsxTunneledNodeIp_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 2),
    _WlsxTunneledNodeIp_Type()
)
wlsxTunneledNodeIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTunneledNodeIp.setStatus("current")
_WlsxNumTunnels_Type = Integer32
_WlsxNumTunnels_Object = MibTableColumn
wlsxNumTunnels = _WlsxNumTunnels_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 3),
    _WlsxNumTunnels_Type()
)
wlsxNumTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxNumTunnels.setStatus("current")


class _WlsxTunneledNodeType_Type(Integer32):
    """Custom type wlsxTunneledNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("others", 1),
          ("corvina", 2))
    )


_WlsxTunneledNodeType_Type.__name__ = "Integer32"
_WlsxTunneledNodeType_Object = MibTableColumn
wlsxTunneledNodeType = _WlsxTunneledNodeType_Object(
    (1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 4),
    _WlsxTunneledNodeType_Type()
)
wlsxTunneledNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wlsxTunneledNodeType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WLSX-TUNNELEDNODE-MIB",
    **{"wlsxTunneledNodeMIB": wlsxTunneledNodeMIB,
       "wlsxTunneledNodeOpGroup": wlsxTunneledNodeOpGroup,
       "wlsxTunneledNodeRequestTable": wlsxTunneledNodeRequestTable,
       "wlsxTunneledNodeRequestEntry": wlsxTunneledNodeRequestEntry,
       "wlsxTunneledNodeMAC": wlsxTunneledNodeMAC,
       "wlsxTunneledNodeIp": wlsxTunneledNodeIp,
       "wlsxNumTunnels": wlsxNumTunnels,
       "wlsxTunneledNodeType": wlsxTunneledNodeType}
)
