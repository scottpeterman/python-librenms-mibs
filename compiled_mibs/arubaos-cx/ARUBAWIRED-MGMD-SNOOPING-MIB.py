# SNMP MIB module (ARUBAWIRED-MGMD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arubaos-cx\ARUBAWIRED-MGMD-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:19:17 2025
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

(wndFeatures,) = mibBuilder.importSymbols(
    "ARUBAWIRED-NETWORKING-OID",
    "wndFeatures")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

arubaWiredMgmdSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingMIB.setRevisions(
        ("2017-11-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MgmdSnoopingGroupTypeDefinition(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filtered", 1),
          ("static", 2))
    )



class MgmdSnoopingConfigPortModeType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("blocked", 2),
          ("forward", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ArubaWiredMgmdSnoopingObjects_ObjectIdentity = ObjectIdentity
arubaWiredMgmdSnoopingObjects = _ArubaWiredMgmdSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1)
)


class _ArubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast_Type(TruthValue):
    """Custom type arubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast based on TruthValue"""
    defaultValue = 1


_ArubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast_Type.__name__ = "TruthValue"
_ArubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast_Object = MibScalar
arubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast = _ArubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 1),
    _ArubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast_Type()
)
arubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast.setStatus("current")
_ArubaWiredMgmdIgmpSnoopingEnabledVLANCount_Type = Unsigned32
_ArubaWiredMgmdIgmpSnoopingEnabledVLANCount_Object = MibScalar
arubaWiredMgmdIgmpSnoopingEnabledVLANCount = _ArubaWiredMgmdIgmpSnoopingEnabledVLANCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 2),
    _ArubaWiredMgmdIgmpSnoopingEnabledVLANCount_Type()
)
arubaWiredMgmdIgmpSnoopingEnabledVLANCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdIgmpSnoopingEnabledVLANCount.setStatus("current")
_ArubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount_Object = MibScalar
arubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount = _ArubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 3),
    _ArubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount_Type()
)
arubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount_Object = MibScalar
arubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount = _ArubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 4),
    _ArubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount_Type()
)
arubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount_Object = MibScalar
arubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount = _ArubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 5),
    _ArubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount_Type()
)
arubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount_Object = MibScalar
arubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount = _ArubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 6),
    _ArubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount_Type()
)
arubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount.setStatus("current")


class _ArubaWiredMgmdMldSnoopingControlDropUnknownMulticast_Type(TruthValue):
    """Custom type arubaWiredMgmdMldSnoopingControlDropUnknownMulticast based on TruthValue"""
    defaultValue = 1


_ArubaWiredMgmdMldSnoopingControlDropUnknownMulticast_Type.__name__ = "TruthValue"
_ArubaWiredMgmdMldSnoopingControlDropUnknownMulticast_Object = MibScalar
arubaWiredMgmdMldSnoopingControlDropUnknownMulticast = _ArubaWiredMgmdMldSnoopingControlDropUnknownMulticast_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 7),
    _ArubaWiredMgmdMldSnoopingControlDropUnknownMulticast_Type()
)
arubaWiredMgmdMldSnoopingControlDropUnknownMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMgmdMldSnoopingControlDropUnknownMulticast.setStatus("current")
_ArubaWiredMgmdMldSnoopingEnabledVLANCount_Type = Unsigned32
_ArubaWiredMgmdMldSnoopingEnabledVLANCount_Object = MibScalar
arubaWiredMgmdMldSnoopingEnabledVLANCount = _ArubaWiredMgmdMldSnoopingEnabledVLANCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 8),
    _ArubaWiredMgmdMldSnoopingEnabledVLANCount_Type()
)
arubaWiredMgmdMldSnoopingEnabledVLANCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdMldSnoopingEnabledVLANCount.setStatus("current")
_ArubaWiredMgmdMldSnoopingMcastGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdMldSnoopingMcastGroupJoinsCount_Object = MibScalar
arubaWiredMgmdMldSnoopingMcastGroupJoinsCount = _ArubaWiredMgmdMldSnoopingMcastGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 9),
    _ArubaWiredMgmdMldSnoopingMcastGroupJoinsCount_Type()
)
arubaWiredMgmdMldSnoopingMcastGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdMldSnoopingMcastGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount_Object = MibScalar
arubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount = _ArubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 10),
    _ArubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount_Type()
)
arubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount_Object = MibScalar
arubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount = _ArubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 11),
    _ArubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount_Type()
)
arubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount_Type = Unsigned32
_ArubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount_Object = MibScalar
arubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount = _ArubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 12),
    _ArubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount_Type()
)
arubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount.setStatus("current")


class _ArubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption_Type(Integer32):
    """Custom type arubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("alternativePadding", 2),
          ("disabled", 3))
    )


_ArubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption_Type.__name__ = "Integer32"
_ArubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption_Object = MibScalar
arubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption = _ArubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 13),
    _ArubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption_Type()
)
arubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption.setStatus("current")
_ArubaWiredMgmdSnoopingVlanTable_Object = MibTable
arubaWiredMgmdSnoopingVlanTable = _ArubaWiredMgmdSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanTable.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntry_Object = MibTableRow
arubaWiredMgmdSnoopingVlanEntry = _ArubaWiredMgmdSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1)
)
arubaWiredMgmdSnoopingVlanEntry.setIndexNames(
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryVid"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryType"),
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntry.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryVid_Type = Unsigned32
_ArubaWiredMgmdSnoopingVlanEntryVid_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryVid = _ArubaWiredMgmdSnoopingVlanEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 1),
    _ArubaWiredMgmdSnoopingVlanEntryVid_Type()
)
arubaWiredMgmdSnoopingVlanEntryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryVid.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryType_Type = InetAddressType
_ArubaWiredMgmdSnoopingVlanEntryType_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryType = _ArubaWiredMgmdSnoopingVlanEntryType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 2),
    _ArubaWiredMgmdSnoopingVlanEntryType_Type()
)
arubaWiredMgmdSnoopingVlanEntryType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryType.setStatus("current")


class _ArubaWiredMgmdSnoopingVlanEntrySnoopingFeature_Type(TruthValue):
    """Custom type arubaWiredMgmdSnoopingVlanEntrySnoopingFeature based on TruthValue"""
    defaultValue = 2


_ArubaWiredMgmdSnoopingVlanEntrySnoopingFeature_Type.__name__ = "TruthValue"
_ArubaWiredMgmdSnoopingVlanEntrySnoopingFeature_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntrySnoopingFeature = _ArubaWiredMgmdSnoopingVlanEntrySnoopingFeature_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 3),
    _ArubaWiredMgmdSnoopingVlanEntrySnoopingFeature_Type()
)
arubaWiredMgmdSnoopingVlanEntrySnoopingFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntrySnoopingFeature.setStatus("current")


class _ArubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus_Type(TruthValue):
    """Custom type arubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus based on TruthValue"""
    defaultValue = 2


_ArubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus_Type.__name__ = "TruthValue"
_ArubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus = _ArubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 4),
    _ArubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus_Type()
)
arubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryQuerierPort_Type = Unsigned32
_ArubaWiredMgmdSnoopingVlanEntryQuerierPort_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryQuerierPort = _ArubaWiredMgmdSnoopingVlanEntryQuerierPort_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 5),
    _ArubaWiredMgmdSnoopingVlanEntryQuerierPort_Type()
)
arubaWiredMgmdSnoopingVlanEntryQuerierPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryQuerierPort.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryFilteredJoins_Type = Unsigned32
_ArubaWiredMgmdSnoopingVlanEntryFilteredJoins_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryFilteredJoins = _ArubaWiredMgmdSnoopingVlanEntryFilteredJoins_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 6),
    _ArubaWiredMgmdSnoopingVlanEntryFilteredJoins_Type()
)
arubaWiredMgmdSnoopingVlanEntryFilteredJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryFilteredJoins.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter_Type = PortList
_ArubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter = _ArubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 7),
    _ArubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter_Type()
)
arubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx = _ArubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 8),
    _ArubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatGSQRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatGSQRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatGSQRx = _ArubaWiredMgmdSnoopingVlanEntryStatGSQRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 9),
    _ArubaWiredMgmdSnoopingVlanEntryStatGSQRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatGSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatGSQRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV1ReportRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV1ReportRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV1ReportRx = _ArubaWiredMgmdSnoopingVlanEntryStatV1ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 10),
    _ArubaWiredMgmdSnoopingVlanEntryStatV1ReportRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV1ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV1ReportRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV2ReportRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV2ReportRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV2ReportRx = _ArubaWiredMgmdSnoopingVlanEntryStatV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 11),
    _ArubaWiredMgmdSnoopingVlanEntryStatV2ReportRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV2ReportRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV3ReportRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV3ReportRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV3ReportRx = _ArubaWiredMgmdSnoopingVlanEntryStatV3ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 12),
    _ArubaWiredMgmdSnoopingVlanEntryStatV3ReportRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV3ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV3ReportRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx = _ArubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 13),
    _ArubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx = _ArubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 14),
    _ArubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx = _ArubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 15),
    _ArubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx = _ArubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 16),
    _ArubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts = _ArubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 17),
    _ArubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStaticJoins_Type = Unsigned32
_ArubaWiredMgmdSnoopingVlanEntryStaticJoins_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStaticJoins = _ArubaWiredMgmdSnoopingVlanEntryStaticJoins_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 18),
    _ArubaWiredMgmdSnoopingVlanEntryStaticJoins_Type()
)
arubaWiredMgmdSnoopingVlanEntryStaticJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStaticJoins.setStatus("current")


class _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval_Type(Unsigned32):
    """Custom type arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ArubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval_Type.__name__ = "Unsigned32"
_ArubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval = _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 19),
    _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval_Type()
)
arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval.setStatus("current")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval.setUnits("seconds")
_ArubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime = _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 20),
    _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime_Type()
)
arubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime.setStatus("current")


class _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness_Type(Unsigned32):
    """Custom type arubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ArubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness_Type.__name__ = "Unsigned32"
_ArubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness = _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 21),
    _ArubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness_Type()
)
arubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount = _ArubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 22),
    _ArubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount = _ArubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 23),
    _ArubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount = _ArubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 24),
    _ArubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount = _ArubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 25),
    _ArubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV1QueryRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV1QueryRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV1QueryRx = _ArubaWiredMgmdSnoopingVlanEntryStatV1QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 26),
    _ArubaWiredMgmdSnoopingVlanEntryStatV1QueryRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV1QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV1QueryRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV2QueryRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV2QueryRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV2QueryRx = _ArubaWiredMgmdSnoopingVlanEntryStatV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 27),
    _ArubaWiredMgmdSnoopingVlanEntryStatV2QueryRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV2QueryRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV3QueryRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV3QueryRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV3QueryRx = _ArubaWiredMgmdSnoopingVlanEntryStatV3QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 28),
    _ArubaWiredMgmdSnoopingVlanEntryStatV3QueryRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV3QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV3QueryRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatGSSQRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatGSSQRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatGSSQRx = _ArubaWiredMgmdSnoopingVlanEntryStatGSSQRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 29),
    _ArubaWiredMgmdSnoopingVlanEntryStatGSSQRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatGSSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatGSSQRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx = _ArubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 30),
    _ArubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx = _ArubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 31),
    _ArubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx = _ArubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 32),
    _ArubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled = _ArubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 33),
    _ArubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV2GSQRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV2GSQRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV2GSQRx = _ArubaWiredMgmdSnoopingVlanEntryStatV2GSQRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 34),
    _ArubaWiredMgmdSnoopingVlanEntryStatV2GSQRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV2GSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV2GSQRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatV3GSQRx_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatV3GSQRx_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatV3GSQRx = _ArubaWiredMgmdSnoopingVlanEntryStatV3GSQRx_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 35),
    _ArubaWiredMgmdSnoopingVlanEntryStatV3GSQRx_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatV3GSQRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatV3GSQRx.setStatus("current")
_ArubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries_Type = Counter32
_ArubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries_Object = MibTableColumn
arubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries = _ArubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 14, 1, 36),
    _ArubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries_Type()
)
arubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries.setStatus("current")
_ArubaWiredMgmdSnoopingCacheTable_Object = MibTable
arubaWiredMgmdSnoopingCacheTable = _ArubaWiredMgmdSnoopingCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheTable.setStatus("current")
_ArubaWiredMgmdSnoopingCacheEntry_Object = MibTableRow
arubaWiredMgmdSnoopingCacheEntry = _ArubaWiredMgmdSnoopingCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1)
)
arubaWiredMgmdSnoopingCacheEntry.setIndexNames(
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheVid"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheAddressType"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheAddress"),
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheEntry.setStatus("current")
_ArubaWiredMgmdSnoopingCacheVid_Type = Unsigned32
_ArubaWiredMgmdSnoopingCacheVid_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheVid = _ArubaWiredMgmdSnoopingCacheVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 1),
    _ArubaWiredMgmdSnoopingCacheVid_Type()
)
arubaWiredMgmdSnoopingCacheVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheVid.setStatus("current")
_ArubaWiredMgmdSnoopingCacheAddressType_Type = InetAddressType
_ArubaWiredMgmdSnoopingCacheAddressType_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheAddressType = _ArubaWiredMgmdSnoopingCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 2),
    _ArubaWiredMgmdSnoopingCacheAddressType_Type()
)
arubaWiredMgmdSnoopingCacheAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheAddressType.setStatus("current")
_ArubaWiredMgmdSnoopingCacheAddress_Type = InetAddress
_ArubaWiredMgmdSnoopingCacheAddress_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheAddress = _ArubaWiredMgmdSnoopingCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 3),
    _ArubaWiredMgmdSnoopingCacheAddress_Type()
)
arubaWiredMgmdSnoopingCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheAddress.setStatus("current")


class _ArubaWiredMgmdSnoopingCacheSelf_Type(TruthValue):
    """Custom type arubaWiredMgmdSnoopingCacheSelf based on TruthValue"""
    defaultValue = 1


_ArubaWiredMgmdSnoopingCacheSelf_Type.__name__ = "TruthValue"
_ArubaWiredMgmdSnoopingCacheSelf_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheSelf = _ArubaWiredMgmdSnoopingCacheSelf_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 4),
    _ArubaWiredMgmdSnoopingCacheSelf_Type()
)
arubaWiredMgmdSnoopingCacheSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheSelf.setStatus("current")
_ArubaWiredMgmdSnoopingCacheLastReporter_Type = InetAddress
_ArubaWiredMgmdSnoopingCacheLastReporter_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheLastReporter = _ArubaWiredMgmdSnoopingCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 5),
    _ArubaWiredMgmdSnoopingCacheLastReporter_Type()
)
arubaWiredMgmdSnoopingCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheLastReporter.setStatus("current")
_ArubaWiredMgmdSnoopingCacheUpTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingCacheUpTime_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheUpTime = _ArubaWiredMgmdSnoopingCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 6),
    _ArubaWiredMgmdSnoopingCacheUpTime_Type()
)
arubaWiredMgmdSnoopingCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheUpTime.setStatus("current")
_ArubaWiredMgmdSnoopingCacheExpiryTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingCacheExpiryTime_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheExpiryTime = _ArubaWiredMgmdSnoopingCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 7),
    _ArubaWiredMgmdSnoopingCacheExpiryTime_Type()
)
arubaWiredMgmdSnoopingCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheExpiryTime.setStatus("current")
_ArubaWiredMgmdSnoopingCacheGroupType_Type = MgmdSnoopingGroupTypeDefinition
_ArubaWiredMgmdSnoopingCacheGroupType_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheGroupType = _ArubaWiredMgmdSnoopingCacheGroupType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 8),
    _ArubaWiredMgmdSnoopingCacheGroupType_Type()
)
arubaWiredMgmdSnoopingCacheGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheGroupType.setStatus("current")
_ArubaWiredMgmdSnoopingCacheJoinedPorts_Type = PortList
_ArubaWiredMgmdSnoopingCacheJoinedPorts_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheJoinedPorts = _ArubaWiredMgmdSnoopingCacheJoinedPorts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 9),
    _ArubaWiredMgmdSnoopingCacheJoinedPorts_Type()
)
arubaWiredMgmdSnoopingCacheJoinedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheJoinedPorts.setStatus("current")
_ArubaWiredMgmdSnoopingCacheStatus_Type = RowStatus
_ArubaWiredMgmdSnoopingCacheStatus_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheStatus = _ArubaWiredMgmdSnoopingCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 10),
    _ArubaWiredMgmdSnoopingCacheStatus_Type()
)
arubaWiredMgmdSnoopingCacheStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheStatus.setStatus("current")
_ArubaWiredMgmdSnoopingCacheQueriesRcvd_Type = Counter32
_ArubaWiredMgmdSnoopingCacheQueriesRcvd_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheQueriesRcvd = _ArubaWiredMgmdSnoopingCacheQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 11),
    _ArubaWiredMgmdSnoopingCacheQueriesRcvd_Type()
)
arubaWiredMgmdSnoopingCacheQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheQueriesRcvd.setStatus("current")
_ArubaWiredMgmdSnoopingCacheJoinsRcvd_Type = Counter32
_ArubaWiredMgmdSnoopingCacheJoinsRcvd_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheJoinsRcvd = _ArubaWiredMgmdSnoopingCacheJoinsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 12),
    _ArubaWiredMgmdSnoopingCacheJoinsRcvd_Type()
)
arubaWiredMgmdSnoopingCacheJoinsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheJoinsRcvd.setStatus("current")


class _ArubaWiredMgmdSnoopingCacheFilterMode_Type(Integer32):
    """Custom type arubaWiredMgmdSnoopingCacheFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_ArubaWiredMgmdSnoopingCacheFilterMode_Type.__name__ = "Integer32"
_ArubaWiredMgmdSnoopingCacheFilterMode_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheFilterMode = _ArubaWiredMgmdSnoopingCacheFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 13),
    _ArubaWiredMgmdSnoopingCacheFilterMode_Type()
)
arubaWiredMgmdSnoopingCacheFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheFilterMode.setStatus("current")
_ArubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer_Type = TimeTicks
_ArubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer = _ArubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 14),
    _ArubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer_Type()
)
arubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer.setStatus("current")
_ArubaWiredMgmdSnoopingCacheVersion1HostTimer_Type = TimeTicks
_ArubaWiredMgmdSnoopingCacheVersion1HostTimer_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheVersion1HostTimer = _ArubaWiredMgmdSnoopingCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 15),
    _ArubaWiredMgmdSnoopingCacheVersion1HostTimer_Type()
)
arubaWiredMgmdSnoopingCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheVersion1HostTimer.setStatus("current")
_ArubaWiredMgmdSnoopingCacheVersion2HostTimer_Type = TimeTicks
_ArubaWiredMgmdSnoopingCacheVersion2HostTimer_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheVersion2HostTimer = _ArubaWiredMgmdSnoopingCacheVersion2HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 16),
    _ArubaWiredMgmdSnoopingCacheVersion2HostTimer_Type()
)
arubaWiredMgmdSnoopingCacheVersion2HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheVersion2HostTimer.setStatus("current")
_ArubaWiredMgmdSnoopingCacheSrcCount_Type = Counter32
_ArubaWiredMgmdSnoopingCacheSrcCount_Object = MibTableColumn
arubaWiredMgmdSnoopingCacheSrcCount = _ArubaWiredMgmdSnoopingCacheSrcCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 15, 1, 17),
    _ArubaWiredMgmdSnoopingCacheSrcCount_Type()
)
arubaWiredMgmdSnoopingCacheSrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheSrcCount.setStatus("current")
_ArubaWiredMgmdSnoopingPortConfigTable_Object = MibTable
arubaWiredMgmdSnoopingPortConfigTable = _ArubaWiredMgmdSnoopingPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 16)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortConfigTable.setStatus("current")
_ArubaWiredMgmdSnoopingPortConfigEntry_Object = MibTableRow
arubaWiredMgmdSnoopingPortConfigEntry = _ArubaWiredMgmdSnoopingPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 16, 1)
)
arubaWiredMgmdSnoopingPortConfigEntry.setIndexNames(
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortConfigEntryVid"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortConfigEntryIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortConfigEntry.setStatus("current")
_ArubaWiredMgmdSnoopingPortConfigEntryVid_Type = Unsigned32
_ArubaWiredMgmdSnoopingPortConfigEntryVid_Object = MibTableColumn
arubaWiredMgmdSnoopingPortConfigEntryVid = _ArubaWiredMgmdSnoopingPortConfigEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 16, 1, 1),
    _ArubaWiredMgmdSnoopingPortConfigEntryVid_Type()
)
arubaWiredMgmdSnoopingPortConfigEntryVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortConfigEntryVid.setStatus("current")
_ArubaWiredMgmdSnoopingPortConfigEntryIndex_Type = Unsigned32
_ArubaWiredMgmdSnoopingPortConfigEntryIndex_Object = MibTableColumn
arubaWiredMgmdSnoopingPortConfigEntryIndex = _ArubaWiredMgmdSnoopingPortConfigEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 16, 1, 2),
    _ArubaWiredMgmdSnoopingPortConfigEntryIndex_Type()
)
arubaWiredMgmdSnoopingPortConfigEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortConfigEntryIndex.setStatus("current")
_ArubaWiredMgmdSnoopingPortConfigEntryPortModeFeature_Type = MgmdSnoopingConfigPortModeType
_ArubaWiredMgmdSnoopingPortConfigEntryPortModeFeature_Object = MibTableColumn
arubaWiredMgmdSnoopingPortConfigEntryPortModeFeature = _ArubaWiredMgmdSnoopingPortConfigEntryPortModeFeature_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 16, 1, 3),
    _ArubaWiredMgmdSnoopingPortConfigEntryPortModeFeature_Type()
)
arubaWiredMgmdSnoopingPortConfigEntryPortModeFeature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortConfigEntryPortModeFeature.setStatus("current")
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheTable_Object = MibTable
arubaWiredMgmdSnoopingFilteredGroupPortCacheTable = _ArubaWiredMgmdSnoopingFilteredGroupPortCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 17)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCacheTable.setStatus("current")
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheEntry_Object = MibTableRow
arubaWiredMgmdSnoopingFilteredGroupPortCacheEntry = _ArubaWiredMgmdSnoopingFilteredGroupPortCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 17, 1)
)
arubaWiredMgmdSnoopingFilteredGroupPortCacheEntry.setIndexNames(
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingFilteredGroupPortCacheVid"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCacheEntry.setStatus("current")
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheVid_Type = Unsigned32
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheVid_Object = MibTableColumn
arubaWiredMgmdSnoopingFilteredGroupPortCacheVid = _ArubaWiredMgmdSnoopingFilteredGroupPortCacheVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 17, 1, 1),
    _ArubaWiredMgmdSnoopingFilteredGroupPortCacheVid_Type()
)
arubaWiredMgmdSnoopingFilteredGroupPortCacheVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCacheVid.setStatus("current")
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType_Type = InetAddressType
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType_Object = MibTableColumn
arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType = _ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 17, 1, 2),
    _ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType_Type()
)
arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType.setStatus("current")
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress_Type = InetAddress
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress_Object = MibTableColumn
arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress = _ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 17, 1, 3),
    _ArubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress_Type()
)
arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress.setStatus("current")
_ArubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex_Type = Unsigned32
_ArubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex_Object = MibTableColumn
arubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex = _ArubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 17, 1, 4),
    _ArubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex_Type()
)
arubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex.setStatus("current")
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime_Object = MibTableColumn
arubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime = _ArubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 17, 1, 5),
    _ArubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime_Type()
)
arubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListTable_Object = MibTable
arubaWiredMgmdSnoopingSrcListTable = _ArubaWiredMgmdSnoopingSrcListTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListTable.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListEntry_Object = MibTableRow
arubaWiredMgmdSnoopingSrcListEntry = _ArubaWiredMgmdSnoopingSrcListEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1)
)
arubaWiredMgmdSnoopingSrcListEntry.setIndexNames(
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListVid"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListAddressType"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListAddress"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListHostAddress"),
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListEntry.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListVid_Type = Unsigned32
_ArubaWiredMgmdSnoopingSrcListVid_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListVid = _ArubaWiredMgmdSnoopingSrcListVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 1),
    _ArubaWiredMgmdSnoopingSrcListVid_Type()
)
arubaWiredMgmdSnoopingSrcListVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListVid.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListAddressType_Type = InetAddressType
_ArubaWiredMgmdSnoopingSrcListAddressType_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListAddressType = _ArubaWiredMgmdSnoopingSrcListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 2),
    _ArubaWiredMgmdSnoopingSrcListAddressType_Type()
)
arubaWiredMgmdSnoopingSrcListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListAddressType.setStatus("current")


class _ArubaWiredMgmdSnoopingSrcListAddress_Type(InetAddress):
    """Custom type arubaWiredMgmdSnoopingSrcListAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_ArubaWiredMgmdSnoopingSrcListAddress_Type.__name__ = "InetAddress"
_ArubaWiredMgmdSnoopingSrcListAddress_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListAddress = _ArubaWiredMgmdSnoopingSrcListAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 3),
    _ArubaWiredMgmdSnoopingSrcListAddress_Type()
)
arubaWiredMgmdSnoopingSrcListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListAddress.setStatus("current")


class _ArubaWiredMgmdSnoopingSrcListHostAddress_Type(InetAddress):
    """Custom type arubaWiredMgmdSnoopingSrcListHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_ArubaWiredMgmdSnoopingSrcListHostAddress_Type.__name__ = "InetAddress"
_ArubaWiredMgmdSnoopingSrcListHostAddress_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListHostAddress = _ArubaWiredMgmdSnoopingSrcListHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 4),
    _ArubaWiredMgmdSnoopingSrcListHostAddress_Type()
)
arubaWiredMgmdSnoopingSrcListHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListHostAddress.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListPorts_Type = PortList
_ArubaWiredMgmdSnoopingSrcListPorts_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListPorts = _ArubaWiredMgmdSnoopingSrcListPorts_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 5),
    _ArubaWiredMgmdSnoopingSrcListPorts_Type()
)
arubaWiredMgmdSnoopingSrcListPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListPorts.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListExpiry_Type = TimeTicks
_ArubaWiredMgmdSnoopingSrcListExpiry_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListExpiry = _ArubaWiredMgmdSnoopingSrcListExpiry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 6),
    _ArubaWiredMgmdSnoopingSrcListExpiry_Type()
)
arubaWiredMgmdSnoopingSrcListExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListExpiry.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListUpTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingSrcListUpTime_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListUpTime = _ArubaWiredMgmdSnoopingSrcListUpTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 7),
    _ArubaWiredMgmdSnoopingSrcListUpTime_Type()
)
arubaWiredMgmdSnoopingSrcListUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListUpTime.setStatus("current")
_ArubaWiredMgmdSnoopingSrcListType_Type = MgmdSnoopingGroupTypeDefinition
_ArubaWiredMgmdSnoopingSrcListType_Object = MibTableColumn
arubaWiredMgmdSnoopingSrcListType = _ArubaWiredMgmdSnoopingSrcListType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 18, 1, 8),
    _ArubaWiredMgmdSnoopingSrcListType_Type()
)
arubaWiredMgmdSnoopingSrcListType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListType.setStatus("current")
_ArubaWiredMgmdSnoopingPortSrcTable_Object = MibTable
arubaWiredMgmdSnoopingPortSrcTable = _ArubaWiredMgmdSnoopingPortSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcTable.setStatus("current")
_ArubaWiredMgmdSnoopingPortSrcEntry_Object = MibTableRow
arubaWiredMgmdSnoopingPortSrcEntry = _ArubaWiredMgmdSnoopingPortSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1)
)
arubaWiredMgmdSnoopingPortSrcEntry.setIndexNames(
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcVid"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcAddressType"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcAddress"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcHostAddress"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcPortIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcEntry.setStatus("current")
_ArubaWiredMgmdSnoopingPortSrcVid_Type = Unsigned32
_ArubaWiredMgmdSnoopingPortSrcVid_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcVid = _ArubaWiredMgmdSnoopingPortSrcVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 1),
    _ArubaWiredMgmdSnoopingPortSrcVid_Type()
)
arubaWiredMgmdSnoopingPortSrcVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcVid.setStatus("current")
_ArubaWiredMgmdSnoopingPortSrcAddressType_Type = InetAddressType
_ArubaWiredMgmdSnoopingPortSrcAddressType_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcAddressType = _ArubaWiredMgmdSnoopingPortSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 2),
    _ArubaWiredMgmdSnoopingPortSrcAddressType_Type()
)
arubaWiredMgmdSnoopingPortSrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcAddressType.setStatus("current")


class _ArubaWiredMgmdSnoopingPortSrcAddress_Type(InetAddress):
    """Custom type arubaWiredMgmdSnoopingPortSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_ArubaWiredMgmdSnoopingPortSrcAddress_Type.__name__ = "InetAddress"
_ArubaWiredMgmdSnoopingPortSrcAddress_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcAddress = _ArubaWiredMgmdSnoopingPortSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 3),
    _ArubaWiredMgmdSnoopingPortSrcAddress_Type()
)
arubaWiredMgmdSnoopingPortSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcAddress.setStatus("current")


class _ArubaWiredMgmdSnoopingPortSrcHostAddress_Type(InetAddress):
    """Custom type arubaWiredMgmdSnoopingPortSrcHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_ArubaWiredMgmdSnoopingPortSrcHostAddress_Type.__name__ = "InetAddress"
_ArubaWiredMgmdSnoopingPortSrcHostAddress_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcHostAddress = _ArubaWiredMgmdSnoopingPortSrcHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 4),
    _ArubaWiredMgmdSnoopingPortSrcHostAddress_Type()
)
arubaWiredMgmdSnoopingPortSrcHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcHostAddress.setStatus("current")
_ArubaWiredMgmdSnoopingPortSrcPortIndex_Type = Unsigned32
_ArubaWiredMgmdSnoopingPortSrcPortIndex_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcPortIndex = _ArubaWiredMgmdSnoopingPortSrcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 5),
    _ArubaWiredMgmdSnoopingPortSrcPortIndex_Type()
)
arubaWiredMgmdSnoopingPortSrcPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcPortIndex.setStatus("current")
_ArubaWiredMgmdSnoopingPortSrcExpiry_Type = TimeTicks
_ArubaWiredMgmdSnoopingPortSrcExpiry_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcExpiry = _ArubaWiredMgmdSnoopingPortSrcExpiry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 6),
    _ArubaWiredMgmdSnoopingPortSrcExpiry_Type()
)
arubaWiredMgmdSnoopingPortSrcExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcExpiry.setStatus("current")
_ArubaWiredMgmdSnoopingPortSrcUpTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingPortSrcUpTime_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcUpTime = _ArubaWiredMgmdSnoopingPortSrcUpTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 7),
    _ArubaWiredMgmdSnoopingPortSrcUpTime_Type()
)
arubaWiredMgmdSnoopingPortSrcUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcUpTime.setStatus("current")


class _ArubaWiredMgmdSnoopingPortSrcFilterMode_Type(Integer32):
    """Custom type arubaWiredMgmdSnoopingPortSrcFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_ArubaWiredMgmdSnoopingPortSrcFilterMode_Type.__name__ = "Integer32"
_ArubaWiredMgmdSnoopingPortSrcFilterMode_Object = MibTableColumn
arubaWiredMgmdSnoopingPortSrcFilterMode = _ArubaWiredMgmdSnoopingPortSrcFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 19, 1, 8),
    _ArubaWiredMgmdSnoopingPortSrcFilterMode_Type()
)
arubaWiredMgmdSnoopingPortSrcFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcFilterMode.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheTable_Object = MibTable
arubaWiredMgmdSnoopingGroupPortCacheTable = _ArubaWiredMgmdSnoopingGroupPortCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20)
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheTable.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheEntry_Object = MibTableRow
arubaWiredMgmdSnoopingGroupPortCacheEntry = _ArubaWiredMgmdSnoopingGroupPortCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1)
)
arubaWiredMgmdSnoopingGroupPortCacheEntry.setIndexNames(
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheVid"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheGroupAddressType"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheGroupAddress"),
    (0, "ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCachePortIndex"),
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheEntry.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheVid_Type = Unsigned32
_ArubaWiredMgmdSnoopingGroupPortCacheVid_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheVid = _ArubaWiredMgmdSnoopingGroupPortCacheVid_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 1),
    _ArubaWiredMgmdSnoopingGroupPortCacheVid_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheVid.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheGroupAddressType_Type = InetAddressType
_ArubaWiredMgmdSnoopingGroupPortCacheGroupAddressType_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheGroupAddressType = _ArubaWiredMgmdSnoopingGroupPortCacheGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 2),
    _ArubaWiredMgmdSnoopingGroupPortCacheGroupAddressType_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheGroupAddressType.setStatus("current")


class _ArubaWiredMgmdSnoopingGroupPortCacheGroupAddress_Type(InetAddress):
    """Custom type arubaWiredMgmdSnoopingGroupPortCacheGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_ArubaWiredMgmdSnoopingGroupPortCacheGroupAddress_Type.__name__ = "InetAddress"
_ArubaWiredMgmdSnoopingGroupPortCacheGroupAddress_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheGroupAddress = _ArubaWiredMgmdSnoopingGroupPortCacheGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 3),
    _ArubaWiredMgmdSnoopingGroupPortCacheGroupAddress_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheGroupAddress.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCachePortIndex_Type = Unsigned32
_ArubaWiredMgmdSnoopingGroupPortCachePortIndex_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCachePortIndex = _ArubaWiredMgmdSnoopingGroupPortCachePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 4),
    _ArubaWiredMgmdSnoopingGroupPortCachePortIndex_Type()
)
arubaWiredMgmdSnoopingGroupPortCachePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCachePortIndex.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheUpTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingGroupPortCacheUpTime_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheUpTime = _ArubaWiredMgmdSnoopingGroupPortCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 5),
    _ArubaWiredMgmdSnoopingGroupPortCacheUpTime_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheUpTime.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheVersion1Timer_Type = TimeTicks
_ArubaWiredMgmdSnoopingGroupPortCacheVersion1Timer_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheVersion1Timer = _ArubaWiredMgmdSnoopingGroupPortCacheVersion1Timer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 6),
    _ArubaWiredMgmdSnoopingGroupPortCacheVersion1Timer_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheVersion1Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheVersion1Timer.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheVersion2Timer_Type = TimeTicks
_ArubaWiredMgmdSnoopingGroupPortCacheVersion2Timer_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheVersion2Timer = _ArubaWiredMgmdSnoopingGroupPortCacheVersion2Timer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 7),
    _ArubaWiredMgmdSnoopingGroupPortCacheVersion2Timer_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheVersion2Timer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheVersion2Timer.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheFilterTimer_Type = TimeTicks
_ArubaWiredMgmdSnoopingGroupPortCacheFilterTimer_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheFilterTimer = _ArubaWiredMgmdSnoopingGroupPortCacheFilterTimer_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 8),
    _ArubaWiredMgmdSnoopingGroupPortCacheFilterTimer_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheFilterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheFilterTimer.setStatus("current")


class _ArubaWiredMgmdSnoopingGroupPortCacheFilterMode_Type(Integer32):
    """Custom type arubaWiredMgmdSnoopingGroupPortCacheFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_ArubaWiredMgmdSnoopingGroupPortCacheFilterMode_Type.__name__ = "Integer32"
_ArubaWiredMgmdSnoopingGroupPortCacheFilterMode_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheFilterMode = _ArubaWiredMgmdSnoopingGroupPortCacheFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 9),
    _ArubaWiredMgmdSnoopingGroupPortCacheFilterMode_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheFilterMode.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount_Type = Counter32
_ArubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount = _ArubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 10),
    _ArubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount_Type = Counter32
_ArubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount = _ArubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 11),
    _ArubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount.setStatus("current")
_ArubaWiredMgmdSnoopingGroupPortCacheExpiryTime_Type = TimeTicks
_ArubaWiredMgmdSnoopingGroupPortCacheExpiryTime_Object = MibTableColumn
arubaWiredMgmdSnoopingGroupPortCacheExpiryTime = _ArubaWiredMgmdSnoopingGroupPortCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 1, 20, 1, 12),
    _ArubaWiredMgmdSnoopingGroupPortCacheExpiryTime_Type()
)
arubaWiredMgmdSnoopingGroupPortCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGroupPortCacheExpiryTime.setStatus("current")
_ArubaWiredMgmdSnoopingConformance_ObjectIdentity = ObjectIdentity
arubaWiredMgmdSnoopingConformance = _ArubaWiredMgmdSnoopingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2)
)
_ArubaWiredMgmdSnoopingGroups_ObjectIdentity = ObjectIdentity
arubaWiredMgmdSnoopingGroups = _ArubaWiredMgmdSnoopingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1)
)
_ArubaWiredMgmdSnoopingCompliances_ObjectIdentity = ObjectIdentity
arubaWiredMgmdSnoopingCompliances = _ArubaWiredMgmdSnoopingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 2)
)

# Managed Objects groups

arubaWiredMgmdSnoopingBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 1)
)
arubaWiredMgmdSnoopingBaseGroup.setObjects(
      *(("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdIgmpSnoopingEnabledVLANCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdMldSnoopingControlDropUnknownMulticast"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdMldSnoopingEnabledVLANCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdMldSnoopingMcastGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption"))
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingBaseGroup.setStatus("current")

arubaWiredMgmdSnoopingVlanEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 2)
)
arubaWiredMgmdSnoopingVlanEntryGroup.setObjects(
      *(("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntrySnoopingFeature"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryQuerierPort"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryFilteredJoins"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatGSQRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV1ReportRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV2ReportRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV3ReportRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStaticJoins"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV1QueryRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV2QueryRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV3QueryRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatGSSQRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV2GSQRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatV3GSQRx"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries"))
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingVlanEntryGroup.setStatus("current")

arubaWiredMgmdSnoopingCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 3)
)
arubaWiredMgmdSnoopingCacheGroup.setObjects(
      *(("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheSelf"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheLastReporter"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheUpTime"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheExpiryTime"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheGroupType"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheJoinedPorts"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheStatus"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheQueriesRcvd"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheJoinsRcvd"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheFilterMode"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheVersion1HostTimer"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheVersion2HostTimer"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheSrcCount"))
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingCacheGroup.setStatus("current")

arubaWiredMgmdSnoopingPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 4)
)
arubaWiredMgmdSnoopingPortGroup.setObjects(
    ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortConfigEntryPortModeFeature")
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortGroup.setStatus("current")

arubaWiredMgmdSnoopingFilteredGroupPortCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 5)
)
arubaWiredMgmdSnoopingFilteredGroupPortCacheGroup.setObjects(
    ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime")
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingFilteredGroupPortCacheGroup.setStatus("current")

arubaWiredMgmdSnoopingSrcListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 6)
)
arubaWiredMgmdSnoopingSrcListGroup.setObjects(
      *(("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListPorts"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListExpiry"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListUpTime"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListType"))
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingSrcListGroup.setStatus("current")

arubaWiredMgmdSnoopingPortSrcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 7)
)
arubaWiredMgmdSnoopingPortSrcGroup.setObjects(
      *(("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcExpiry"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcUpTime"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcFilterMode"))
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingPortSrcGroup.setStatus("current")

arubaWiredMgmdSnoopingGruoupPortCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 1, 8)
)
arubaWiredMgmdSnoopingGruoupPortCacheGroup.setObjects(
      *(("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheUpTime"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheVersion1Timer"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheVersion2Timer"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheFilterTimer"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheFilterMode"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGroupPortCacheExpiryTime"))
)
if mibBuilder.loadTexts:
    arubaWiredMgmdSnoopingGruoupPortCacheGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

arubaWiredMgmdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47196, 4, 1, 1, 3, 3, 2, 2, 1)
)
arubaWiredMgmdMIBCompliance.setObjects(
      *(("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingBaseGroup"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingVlanEntryGroup"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingCacheGroup"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortGroup"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingFilteredGroupPortCacheGroup"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingGruoupPortCacheGroup"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingSrcListGroup"),
        ("ARUBAWIRED-MGMD-SNOOPING-MIB", "arubaWiredMgmdSnoopingPortSrcGroup"))
)
if mibBuilder.loadTexts:
    arubaWiredMgmdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARUBAWIRED-MGMD-SNOOPING-MIB",
    **{"MgmdSnoopingGroupTypeDefinition": MgmdSnoopingGroupTypeDefinition,
       "MgmdSnoopingConfigPortModeType": MgmdSnoopingConfigPortModeType,
       "arubaWiredMgmdSnoopingMIB": arubaWiredMgmdSnoopingMIB,
       "arubaWiredMgmdSnoopingObjects": arubaWiredMgmdSnoopingObjects,
       "arubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast": arubaWiredMgmdIgmpSnoopingControlDropUnknownMulticast,
       "arubaWiredMgmdIgmpSnoopingEnabledVLANCount": arubaWiredMgmdIgmpSnoopingEnabledVLANCount,
       "arubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount": arubaWiredMgmdIgmpSnoopingMcastGroupJoinsCount,
       "arubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount": arubaWiredMgmdIgmpSnoopingMcastFilteredGroupJoinsCount,
       "arubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount": arubaWiredMgmdIgmpSnoopingMcastExcludeGroupJoinsCount,
       "arubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount": arubaWiredMgmdIgmpSnoopingMcastIncludeGroupJoinsCount,
       "arubaWiredMgmdMldSnoopingControlDropUnknownMulticast": arubaWiredMgmdMldSnoopingControlDropUnknownMulticast,
       "arubaWiredMgmdMldSnoopingEnabledVLANCount": arubaWiredMgmdMldSnoopingEnabledVLANCount,
       "arubaWiredMgmdMldSnoopingMcastGroupJoinsCount": arubaWiredMgmdMldSnoopingMcastGroupJoinsCount,
       "arubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount": arubaWiredMgmdMldSnoopingMcastExcludeGroupJoinsCount,
       "arubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount": arubaWiredMgmdMldSnoopingMcastIncludeGroupJoinsCount,
       "arubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount": arubaWiredMgmdMldSnoopingMcastFilteredGroupJoinsCount,
       "arubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption": arubaWiredMgmdMldSnoopingSendRouterAlertPaddingOption,
       "arubaWiredMgmdSnoopingVlanTable": arubaWiredMgmdSnoopingVlanTable,
       "arubaWiredMgmdSnoopingVlanEntry": arubaWiredMgmdSnoopingVlanEntry,
       "arubaWiredMgmdSnoopingVlanEntryVid": arubaWiredMgmdSnoopingVlanEntryVid,
       "arubaWiredMgmdSnoopingVlanEntryType": arubaWiredMgmdSnoopingVlanEntryType,
       "arubaWiredMgmdSnoopingVlanEntrySnoopingFeature": arubaWiredMgmdSnoopingVlanEntrySnoopingFeature,
       "arubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus": arubaWiredMgmdSnoopingVlanEntryControlDropUnknownMulticastStatus,
       "arubaWiredMgmdSnoopingVlanEntryQuerierPort": arubaWiredMgmdSnoopingVlanEntryQuerierPort,
       "arubaWiredMgmdSnoopingVlanEntryFilteredJoins": arubaWiredMgmdSnoopingVlanEntryFilteredJoins,
       "arubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter": arubaWiredMgmdSnoopingVlanEntryPortsWithMcastRouter,
       "arubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx": arubaWiredMgmdSnoopingVlanEntryStatGeneralQueryRx,
       "arubaWiredMgmdSnoopingVlanEntryStatGSQRx": arubaWiredMgmdSnoopingVlanEntryStatGSQRx,
       "arubaWiredMgmdSnoopingVlanEntryStatV1ReportRx": arubaWiredMgmdSnoopingVlanEntryStatV1ReportRx,
       "arubaWiredMgmdSnoopingVlanEntryStatV2ReportRx": arubaWiredMgmdSnoopingVlanEntryStatV2ReportRx,
       "arubaWiredMgmdSnoopingVlanEntryStatV3ReportRx": arubaWiredMgmdSnoopingVlanEntryStatV3ReportRx,
       "arubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx": arubaWiredMgmdSnoopingVlanEntryStatV2LeaveRx,
       "arubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx": arubaWiredMgmdSnoopingVlanEntryStatUnknownTypeRx,
       "arubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx": arubaWiredMgmdSnoopingVlanEntryStatForwardToRoutersTx,
       "arubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx": arubaWiredMgmdSnoopingVlanEntryStatForwardToAllPortsTx,
       "arubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts": arubaWiredMgmdSnoopingVlanEntryStatJoinTimeouts,
       "arubaWiredMgmdSnoopingVlanEntryStaticJoins": arubaWiredMgmdSnoopingVlanEntryStaticJoins,
       "arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval": arubaWiredMgmdSnoopingVlanEntryOtherQuerierInterval,
       "arubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime": arubaWiredMgmdSnoopingVlanEntryOtherQuerierExpiryTime,
       "arubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness": arubaWiredMgmdSnoopingVlanEntryOtherQuerierRobustness,
       "arubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount": arubaWiredMgmdSnoopingVlanEntryStatExcludeGroupJoinsCount,
       "arubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount": arubaWiredMgmdSnoopingVlanEntryStatIncludeGroupJoinsCount,
       "arubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount": arubaWiredMgmdSnoopingVlanEntryStatFilteredExcludeGroupJoinsCount,
       "arubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount": arubaWiredMgmdSnoopingVlanEntryStatFilteredIncludeGroupJoinsCount,
       "arubaWiredMgmdSnoopingVlanEntryStatV1QueryRx": arubaWiredMgmdSnoopingVlanEntryStatV1QueryRx,
       "arubaWiredMgmdSnoopingVlanEntryStatV2QueryRx": arubaWiredMgmdSnoopingVlanEntryStatV2QueryRx,
       "arubaWiredMgmdSnoopingVlanEntryStatV3QueryRx": arubaWiredMgmdSnoopingVlanEntryStatV3QueryRx,
       "arubaWiredMgmdSnoopingVlanEntryStatGSSQRx": arubaWiredMgmdSnoopingVlanEntryStatGSSQRx,
       "arubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx": arubaWiredMgmdSnoopingVlanEntryStatMalformedPktRx,
       "arubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx": arubaWiredMgmdSnoopingVlanEntryStatBadCheckSumRx,
       "arubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx": arubaWiredMgmdSnoopingVlanEntryStatMartianSourceRx,
       "arubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled": arubaWiredMgmdSnoopingVlanEntryStatPacketsRxOnDisabled,
       "arubaWiredMgmdSnoopingVlanEntryStatV2GSQRx": arubaWiredMgmdSnoopingVlanEntryStatV2GSQRx,
       "arubaWiredMgmdSnoopingVlanEntryStatV3GSQRx": arubaWiredMgmdSnoopingVlanEntryStatV3GSQRx,
       "arubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries": arubaWiredMgmdSnoopingVlanEntryStatWrongVersionQueries,
       "arubaWiredMgmdSnoopingCacheTable": arubaWiredMgmdSnoopingCacheTable,
       "arubaWiredMgmdSnoopingCacheEntry": arubaWiredMgmdSnoopingCacheEntry,
       "arubaWiredMgmdSnoopingCacheVid": arubaWiredMgmdSnoopingCacheVid,
       "arubaWiredMgmdSnoopingCacheAddressType": arubaWiredMgmdSnoopingCacheAddressType,
       "arubaWiredMgmdSnoopingCacheAddress": arubaWiredMgmdSnoopingCacheAddress,
       "arubaWiredMgmdSnoopingCacheSelf": arubaWiredMgmdSnoopingCacheSelf,
       "arubaWiredMgmdSnoopingCacheLastReporter": arubaWiredMgmdSnoopingCacheLastReporter,
       "arubaWiredMgmdSnoopingCacheUpTime": arubaWiredMgmdSnoopingCacheUpTime,
       "arubaWiredMgmdSnoopingCacheExpiryTime": arubaWiredMgmdSnoopingCacheExpiryTime,
       "arubaWiredMgmdSnoopingCacheGroupType": arubaWiredMgmdSnoopingCacheGroupType,
       "arubaWiredMgmdSnoopingCacheJoinedPorts": arubaWiredMgmdSnoopingCacheJoinedPorts,
       "arubaWiredMgmdSnoopingCacheStatus": arubaWiredMgmdSnoopingCacheStatus,
       "arubaWiredMgmdSnoopingCacheQueriesRcvd": arubaWiredMgmdSnoopingCacheQueriesRcvd,
       "arubaWiredMgmdSnoopingCacheJoinsRcvd": arubaWiredMgmdSnoopingCacheJoinsRcvd,
       "arubaWiredMgmdSnoopingCacheFilterMode": arubaWiredMgmdSnoopingCacheFilterMode,
       "arubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer": arubaWiredMgmdSnoopingCacheExcludeModeExpiryTimer,
       "arubaWiredMgmdSnoopingCacheVersion1HostTimer": arubaWiredMgmdSnoopingCacheVersion1HostTimer,
       "arubaWiredMgmdSnoopingCacheVersion2HostTimer": arubaWiredMgmdSnoopingCacheVersion2HostTimer,
       "arubaWiredMgmdSnoopingCacheSrcCount": arubaWiredMgmdSnoopingCacheSrcCount,
       "arubaWiredMgmdSnoopingPortConfigTable": arubaWiredMgmdSnoopingPortConfigTable,
       "arubaWiredMgmdSnoopingPortConfigEntry": arubaWiredMgmdSnoopingPortConfigEntry,
       "arubaWiredMgmdSnoopingPortConfigEntryVid": arubaWiredMgmdSnoopingPortConfigEntryVid,
       "arubaWiredMgmdSnoopingPortConfigEntryIndex": arubaWiredMgmdSnoopingPortConfigEntryIndex,
       "arubaWiredMgmdSnoopingPortConfigEntryPortModeFeature": arubaWiredMgmdSnoopingPortConfigEntryPortModeFeature,
       "arubaWiredMgmdSnoopingFilteredGroupPortCacheTable": arubaWiredMgmdSnoopingFilteredGroupPortCacheTable,
       "arubaWiredMgmdSnoopingFilteredGroupPortCacheEntry": arubaWiredMgmdSnoopingFilteredGroupPortCacheEntry,
       "arubaWiredMgmdSnoopingFilteredGroupPortCacheVid": arubaWiredMgmdSnoopingFilteredGroupPortCacheVid,
       "arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType": arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddressType,
       "arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress": arubaWiredMgmdSnoopingFilteredGroupPortCacheGroupAddress,
       "arubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex": arubaWiredMgmdSnoopingFilteredGroupPortCachePortIndex,
       "arubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime": arubaWiredMgmdSnoopingFilteredGroupPortCacheExpiryTime,
       "arubaWiredMgmdSnoopingSrcListTable": arubaWiredMgmdSnoopingSrcListTable,
       "arubaWiredMgmdSnoopingSrcListEntry": arubaWiredMgmdSnoopingSrcListEntry,
       "arubaWiredMgmdSnoopingSrcListVid": arubaWiredMgmdSnoopingSrcListVid,
       "arubaWiredMgmdSnoopingSrcListAddressType": arubaWiredMgmdSnoopingSrcListAddressType,
       "arubaWiredMgmdSnoopingSrcListAddress": arubaWiredMgmdSnoopingSrcListAddress,
       "arubaWiredMgmdSnoopingSrcListHostAddress": arubaWiredMgmdSnoopingSrcListHostAddress,
       "arubaWiredMgmdSnoopingSrcListPorts": arubaWiredMgmdSnoopingSrcListPorts,
       "arubaWiredMgmdSnoopingSrcListExpiry": arubaWiredMgmdSnoopingSrcListExpiry,
       "arubaWiredMgmdSnoopingSrcListUpTime": arubaWiredMgmdSnoopingSrcListUpTime,
       "arubaWiredMgmdSnoopingSrcListType": arubaWiredMgmdSnoopingSrcListType,
       "arubaWiredMgmdSnoopingPortSrcTable": arubaWiredMgmdSnoopingPortSrcTable,
       "arubaWiredMgmdSnoopingPortSrcEntry": arubaWiredMgmdSnoopingPortSrcEntry,
       "arubaWiredMgmdSnoopingPortSrcVid": arubaWiredMgmdSnoopingPortSrcVid,
       "arubaWiredMgmdSnoopingPortSrcAddressType": arubaWiredMgmdSnoopingPortSrcAddressType,
       "arubaWiredMgmdSnoopingPortSrcAddress": arubaWiredMgmdSnoopingPortSrcAddress,
       "arubaWiredMgmdSnoopingPortSrcHostAddress": arubaWiredMgmdSnoopingPortSrcHostAddress,
       "arubaWiredMgmdSnoopingPortSrcPortIndex": arubaWiredMgmdSnoopingPortSrcPortIndex,
       "arubaWiredMgmdSnoopingPortSrcExpiry": arubaWiredMgmdSnoopingPortSrcExpiry,
       "arubaWiredMgmdSnoopingPortSrcUpTime": arubaWiredMgmdSnoopingPortSrcUpTime,
       "arubaWiredMgmdSnoopingPortSrcFilterMode": arubaWiredMgmdSnoopingPortSrcFilterMode,
       "arubaWiredMgmdSnoopingGroupPortCacheTable": arubaWiredMgmdSnoopingGroupPortCacheTable,
       "arubaWiredMgmdSnoopingGroupPortCacheEntry": arubaWiredMgmdSnoopingGroupPortCacheEntry,
       "arubaWiredMgmdSnoopingGroupPortCacheVid": arubaWiredMgmdSnoopingGroupPortCacheVid,
       "arubaWiredMgmdSnoopingGroupPortCacheGroupAddressType": arubaWiredMgmdSnoopingGroupPortCacheGroupAddressType,
       "arubaWiredMgmdSnoopingGroupPortCacheGroupAddress": arubaWiredMgmdSnoopingGroupPortCacheGroupAddress,
       "arubaWiredMgmdSnoopingGroupPortCachePortIndex": arubaWiredMgmdSnoopingGroupPortCachePortIndex,
       "arubaWiredMgmdSnoopingGroupPortCacheUpTime": arubaWiredMgmdSnoopingGroupPortCacheUpTime,
       "arubaWiredMgmdSnoopingGroupPortCacheVersion1Timer": arubaWiredMgmdSnoopingGroupPortCacheVersion1Timer,
       "arubaWiredMgmdSnoopingGroupPortCacheVersion2Timer": arubaWiredMgmdSnoopingGroupPortCacheVersion2Timer,
       "arubaWiredMgmdSnoopingGroupPortCacheFilterTimer": arubaWiredMgmdSnoopingGroupPortCacheFilterTimer,
       "arubaWiredMgmdSnoopingGroupPortCacheFilterMode": arubaWiredMgmdSnoopingGroupPortCacheFilterMode,
       "arubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount": arubaWiredMgmdSnoopingGroupPortCacheExcludeSrcCount,
       "arubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount": arubaWiredMgmdSnoopingGroupPortCacheRequestedSrcCount,
       "arubaWiredMgmdSnoopingGroupPortCacheExpiryTime": arubaWiredMgmdSnoopingGroupPortCacheExpiryTime,
       "arubaWiredMgmdSnoopingConformance": arubaWiredMgmdSnoopingConformance,
       "arubaWiredMgmdSnoopingGroups": arubaWiredMgmdSnoopingGroups,
       "arubaWiredMgmdSnoopingBaseGroup": arubaWiredMgmdSnoopingBaseGroup,
       "arubaWiredMgmdSnoopingVlanEntryGroup": arubaWiredMgmdSnoopingVlanEntryGroup,
       "arubaWiredMgmdSnoopingCacheGroup": arubaWiredMgmdSnoopingCacheGroup,
       "arubaWiredMgmdSnoopingPortGroup": arubaWiredMgmdSnoopingPortGroup,
       "arubaWiredMgmdSnoopingFilteredGroupPortCacheGroup": arubaWiredMgmdSnoopingFilteredGroupPortCacheGroup,
       "arubaWiredMgmdSnoopingSrcListGroup": arubaWiredMgmdSnoopingSrcListGroup,
       "arubaWiredMgmdSnoopingPortSrcGroup": arubaWiredMgmdSnoopingPortSrcGroup,
       "arubaWiredMgmdSnoopingGruoupPortCacheGroup": arubaWiredMgmdSnoopingGruoupPortCacheGroup,
       "arubaWiredMgmdSnoopingCompliances": arubaWiredMgmdSnoopingCompliances,
       "arubaWiredMgmdMIBCompliance": arubaWiredMgmdMIBCompliance}
)
