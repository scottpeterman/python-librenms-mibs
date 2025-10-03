# SNMP MIB module (DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\microsoft\DHCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:10:34 2025
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

(microsoft,
 software) = mibBuilder.importSymbols(
    "MSFT-MIB",
    "microsoft",
    "software")

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



# MIB Managed Objects in the order of their OIDs

_Dhcp_ObjectIdentity = ObjectIdentity
dhcp = _Dhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 3)
)
_DhcpPar_ObjectIdentity = ObjectIdentity
dhcpPar = _DhcpPar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1)
)


class _ParDhcpStartTime_Type(DisplayString):
    """Custom type parDhcpStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ParDhcpStartTime_Type.__name__ = "DisplayString"
_ParDhcpStartTime_Object = MibScalar
parDhcpStartTime = _ParDhcpStartTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 1),
    _ParDhcpStartTime_Type()
)
parDhcpStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpStartTime.setStatus("mandatory")
_ParDhcpTotalNoOfDiscovers_Type = Counter32
_ParDhcpTotalNoOfDiscovers_Object = MibScalar
parDhcpTotalNoOfDiscovers = _ParDhcpTotalNoOfDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 2),
    _ParDhcpTotalNoOfDiscovers_Type()
)
parDhcpTotalNoOfDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpTotalNoOfDiscovers.setStatus("mandatory")
_ParDhcpTotalNoOfRequests_Type = Counter32
_ParDhcpTotalNoOfRequests_Object = MibScalar
parDhcpTotalNoOfRequests = _ParDhcpTotalNoOfRequests_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 3),
    _ParDhcpTotalNoOfRequests_Type()
)
parDhcpTotalNoOfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpTotalNoOfRequests.setStatus("mandatory")
_ParDhcpTotalNoOfReleases_Type = Counter32
_ParDhcpTotalNoOfReleases_Object = MibScalar
parDhcpTotalNoOfReleases = _ParDhcpTotalNoOfReleases_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 4),
    _ParDhcpTotalNoOfReleases_Type()
)
parDhcpTotalNoOfReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpTotalNoOfReleases.setStatus("mandatory")
_ParDhcpTotalNoOfOffers_Type = Counter32
_ParDhcpTotalNoOfOffers_Object = MibScalar
parDhcpTotalNoOfOffers = _ParDhcpTotalNoOfOffers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 5),
    _ParDhcpTotalNoOfOffers_Type()
)
parDhcpTotalNoOfOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpTotalNoOfOffers.setStatus("mandatory")
_ParDhcpTotalNoOfAcks_Type = Counter32
_ParDhcpTotalNoOfAcks_Object = MibScalar
parDhcpTotalNoOfAcks = _ParDhcpTotalNoOfAcks_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 6),
    _ParDhcpTotalNoOfAcks_Type()
)
parDhcpTotalNoOfAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpTotalNoOfAcks.setStatus("mandatory")
_ParDhcpTotalNoOfNacks_Type = Counter32
_ParDhcpTotalNoOfNacks_Object = MibScalar
parDhcpTotalNoOfNacks = _ParDhcpTotalNoOfNacks_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 7),
    _ParDhcpTotalNoOfNacks_Type()
)
parDhcpTotalNoOfNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpTotalNoOfNacks.setStatus("mandatory")
_ParDhcpTotalNoOfDeclines_Type = Counter32
_ParDhcpTotalNoOfDeclines_Object = MibScalar
parDhcpTotalNoOfDeclines = _ParDhcpTotalNoOfDeclines_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 1, 8),
    _ParDhcpTotalNoOfDeclines_Type()
)
parDhcpTotalNoOfDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parDhcpTotalNoOfDeclines.setStatus("mandatory")
_DhcpScope_ObjectIdentity = ObjectIdentity
dhcpScope = _DhcpScope_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 2)
)
_ScopeTable_Object = MibTable
scopeTable = _ScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    scopeTable.setStatus("mandatory")
_ScopeTableEntry_Object = MibTableRow
scopeTableEntry = _ScopeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 2, 1, 1)
)
scopeTableEntry.setIndexNames(
    (0, "DHCP-MIB", "subnetAdd"),
)
if mibBuilder.loadTexts:
    scopeTableEntry.setStatus("mandatory")
_SubnetAdd_Type = IpAddress
_SubnetAdd_Object = MibTableColumn
subnetAdd = _SubnetAdd_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 2, 1, 1, 1),
    _SubnetAdd_Type()
)
subnetAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetAdd.setStatus("mandatory")
_NoAddInUse_Type = Counter32
_NoAddInUse_Object = MibTableColumn
noAddInUse = _NoAddInUse_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 2, 1, 1, 2),
    _NoAddInUse_Type()
)
noAddInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noAddInUse.setStatus("mandatory")
_NoAddFree_Type = Counter32
_NoAddFree_Object = MibTableColumn
noAddFree = _NoAddFree_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 2, 1, 1, 3),
    _NoAddFree_Type()
)
noAddFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noAddFree.setStatus("mandatory")
_NoPendingOffers_Type = Counter32
_NoPendingOffers_Object = MibTableColumn
noPendingOffers = _NoPendingOffers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 3, 2, 1, 1, 4),
    _NoPendingOffers_Type()
)
noPendingOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noPendingOffers.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-MIB",
    **{"dhcp": dhcp,
       "dhcpPar": dhcpPar,
       "parDhcpStartTime": parDhcpStartTime,
       "parDhcpTotalNoOfDiscovers": parDhcpTotalNoOfDiscovers,
       "parDhcpTotalNoOfRequests": parDhcpTotalNoOfRequests,
       "parDhcpTotalNoOfReleases": parDhcpTotalNoOfReleases,
       "parDhcpTotalNoOfOffers": parDhcpTotalNoOfOffers,
       "parDhcpTotalNoOfAcks": parDhcpTotalNoOfAcks,
       "parDhcpTotalNoOfNacks": parDhcpTotalNoOfNacks,
       "parDhcpTotalNoOfDeclines": parDhcpTotalNoOfDeclines,
       "dhcpScope": dhcpScope,
       "scopeTable": scopeTable,
       "scopeTableEntry": scopeTableEntry,
       "subnetAdd": subnetAdd,
       "noAddInUse": noAddInUse,
       "noAddFree": noAddFree,
       "noPendingOffers": noPendingOffers}
)
