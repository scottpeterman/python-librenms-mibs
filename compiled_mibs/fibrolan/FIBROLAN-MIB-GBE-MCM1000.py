# SNMP MIB module (FIBROLAN-MIB-GBE-MCM1000) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-GBE-MCM1000
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:20 2025
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

(flMsModuleMvChannelEntry,
 flMsModuleMvLinkEntry) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-MSMODULE",
    "flMsModuleMvChannelEntry",
    "flMsModuleMvLinkEntry")

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

flMcm1000Mv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibrolan_ObjectIdentity = ObjectIdentity
fibrolan = _Fibrolan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467)
)
_FibrolanSNMP_ObjectIdentity = ObjectIdentity
fibrolanSNMP = _FibrolanSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100)
)
_FlMetroStarMv_ObjectIdentity = ObjectIdentity
flMetroStarMv = _FlMetroStarMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500)
)
_FlMsChassisMv_ObjectIdentity = ObjectIdentity
flMsChassisMv = _FlMsChassisMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10)
)
_FlMsModuleMv_ObjectIdentity = ObjectIdentity
flMsModuleMv = _FlMsModuleMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30)
)
_FlMcm1000MvMIBConformance_ObjectIdentity = ObjectIdentity
flMcm1000MvMIBConformance = _FlMcm1000MvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 1)
)
_FlMcm1000MvMIBCompliances_ObjectIdentity = ObjectIdentity
flMcm1000MvMIBCompliances = _FlMcm1000MvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 1, 1)
)
_FlMcm1000MvMIBGroups_ObjectIdentity = ObjectIdentity
flMcm1000MvMIBGroups = _FlMcm1000MvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 1, 2)
)
_FlMcm1000ModuleMv_ObjectIdentity = ObjectIdentity
flMcm1000ModuleMv = _FlMcm1000ModuleMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 10)
)
_FlMcm1000ChannelsMv_ObjectIdentity = ObjectIdentity
flMcm1000ChannelsMv = _FlMcm1000ChannelsMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20)
)
_FlMcm1000ChannelExtMvTable_Object = MibTable
flMcm1000ChannelExtMvTable = _FlMcm1000ChannelExtMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1)
)
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvTable.setStatus("current")
_FlMcm1000ChannelExtMvEntry_Object = MibTableRow
flMcm1000ChannelExtMvEntry = _FlMcm1000ChannelExtMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvEntry.setStatus("current")


class _FlMcm1000ChannelExtMvP2Link_Type(Integer32):
    """Custom type flMcm1000ChannelExtMvP2Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000ChannelExtMvP2Link_Type.__name__ = "Integer32"
_FlMcm1000ChannelExtMvP2Link_Object = MibTableColumn
flMcm1000ChannelExtMvP2Link = _FlMcm1000ChannelExtMvP2Link_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 1),
    _FlMcm1000ChannelExtMvP2Link_Type()
)
flMcm1000ChannelExtMvP2Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvP2Link.setStatus("current")


class _FlMcm1000ChannelExtMvP1Link_Type(Integer32):
    """Custom type flMcm1000ChannelExtMvP1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("killed", 3))
    )


_FlMcm1000ChannelExtMvP1Link_Type.__name__ = "Integer32"
_FlMcm1000ChannelExtMvP1Link_Object = MibTableColumn
flMcm1000ChannelExtMvP1Link = _FlMcm1000ChannelExtMvP1Link_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 2),
    _FlMcm1000ChannelExtMvP1Link_Type()
)
flMcm1000ChannelExtMvP1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvP1Link.setStatus("current")
_FlMcm1000ChannelExtMvPortDescription_Type = DisplayString
_FlMcm1000ChannelExtMvPortDescription_Object = MibTableColumn
flMcm1000ChannelExtMvPortDescription = _FlMcm1000ChannelExtMvPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 3),
    _FlMcm1000ChannelExtMvPortDescription_Type()
)
flMcm1000ChannelExtMvPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvPortDescription.setStatus("current")


class _FlMcm1000ChannelExtMvP2SignalDetect_Type(Integer32):
    """Custom type flMcm1000ChannelExtMvP2SignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000ChannelExtMvP2SignalDetect_Type.__name__ = "Integer32"
_FlMcm1000ChannelExtMvP2SignalDetect_Object = MibTableColumn
flMcm1000ChannelExtMvP2SignalDetect = _FlMcm1000ChannelExtMvP2SignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 4),
    _FlMcm1000ChannelExtMvP2SignalDetect_Type()
)
flMcm1000ChannelExtMvP2SignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvP2SignalDetect.setStatus("current")


class _FlMcm1000ChannelExtMvP1SignalDetect_Type(Integer32):
    """Custom type flMcm1000ChannelExtMvP1SignalDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000ChannelExtMvP1SignalDetect_Type.__name__ = "Integer32"
_FlMcm1000ChannelExtMvP1SignalDetect_Object = MibTableColumn
flMcm1000ChannelExtMvP1SignalDetect = _FlMcm1000ChannelExtMvP1SignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 5),
    _FlMcm1000ChannelExtMvP1SignalDetect_Type()
)
flMcm1000ChannelExtMvP1SignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvP1SignalDetect.setStatus("current")


class _FlMcm1000ChannelExtMvChannelEnable_Type(Integer32):
    """Custom type flMcm1000ChannelExtMvChannelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlMcm1000ChannelExtMvChannelEnable_Type.__name__ = "Integer32"
_FlMcm1000ChannelExtMvChannelEnable_Object = MibTableColumn
flMcm1000ChannelExtMvChannelEnable = _FlMcm1000ChannelExtMvChannelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 6),
    _FlMcm1000ChannelExtMvChannelEnable_Type()
)
flMcm1000ChannelExtMvChannelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvChannelEnable.setStatus("current")


class _FlMcm1000ChannelExtMvP2LoopBack_Type(Integer32):
    """Custom type flMcm1000ChannelExtMvP2LoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000ChannelExtMvP2LoopBack_Type.__name__ = "Integer32"
_FlMcm1000ChannelExtMvP2LoopBack_Object = MibTableColumn
flMcm1000ChannelExtMvP2LoopBack = _FlMcm1000ChannelExtMvP2LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 7),
    _FlMcm1000ChannelExtMvP2LoopBack_Type()
)
flMcm1000ChannelExtMvP2LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvP2LoopBack.setStatus("current")


class _FlMcm1000ChannelExtMvP1LoopBack_Type(Integer32):
    """Custom type flMcm1000ChannelExtMvP1LoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000ChannelExtMvP1LoopBack_Type.__name__ = "Integer32"
_FlMcm1000ChannelExtMvP1LoopBack_Object = MibTableColumn
flMcm1000ChannelExtMvP1LoopBack = _FlMcm1000ChannelExtMvP1LoopBack_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 20, 1, 1, 8),
    _FlMcm1000ChannelExtMvP1LoopBack_Type()
)
flMcm1000ChannelExtMvP1LoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000ChannelExtMvP1LoopBack.setStatus("current")
_FlMcm1000LinksMv_ObjectIdentity = ObjectIdentity
flMcm1000LinksMv = _FlMcm1000LinksMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30)
)
_FlMcm1000LinkExtMvTable_Object = MibTable
flMcm1000LinkExtMvTable = _FlMcm1000LinkExtMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1)
)
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvTable.setStatus("current")
_FlMcm1000LinkExtMvEntry_Object = MibTableRow
flMcm1000LinkExtMvEntry = _FlMcm1000LinkExtMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvEntry.setStatus("current")


class _FlMcm1000LinkExtMvUpstreamBw_Type(Integer32):
    """Custom type flMcm1000LinkExtMvUpstreamBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FlMcm1000LinkExtMvUpstreamBw_Type.__name__ = "Integer32"
_FlMcm1000LinkExtMvUpstreamBw_Object = MibTableColumn
flMcm1000LinkExtMvUpstreamBw = _FlMcm1000LinkExtMvUpstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1, 1, 1),
    _FlMcm1000LinkExtMvUpstreamBw_Type()
)
flMcm1000LinkExtMvUpstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvUpstreamBw.setStatus("current")


class _FlMcm1000LinkExtMvDownstreamBw_Type(Integer32):
    """Custom type flMcm1000LinkExtMvDownstreamBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FlMcm1000LinkExtMvDownstreamBw_Type.__name__ = "Integer32"
_FlMcm1000LinkExtMvDownstreamBw_Object = MibTableColumn
flMcm1000LinkExtMvDownstreamBw = _FlMcm1000LinkExtMvDownstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1, 1, 2),
    _FlMcm1000LinkExtMvDownstreamBw_Type()
)
flMcm1000LinkExtMvDownstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvDownstreamBw.setStatus("current")


class _FlMcm1000LinkExtMvP2_P1Lst_Type(Integer32):
    """Custom type flMcm1000LinkExtMvP2_P1Lst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000LinkExtMvP2_P1Lst_Type.__name__ = "Integer32"
_FlMcm1000LinkExtMvP2_P1Lst_Object = MibTableColumn
flMcm1000LinkExtMvP2_P1Lst = _FlMcm1000LinkExtMvP2_P1Lst_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1, 1, 3),
    _FlMcm1000LinkExtMvP2_P1Lst_Type()
)
flMcm1000LinkExtMvP2_P1Lst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvP2_P1Lst.setStatus("current")


class _FlMcm1000LinkExtMvP1_P2Lst_Type(Integer32):
    """Custom type flMcm1000LinkExtMvP1_P2Lst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000LinkExtMvP1_P2Lst_Type.__name__ = "Integer32"
_FlMcm1000LinkExtMvP1_P2Lst_Object = MibTableColumn
flMcm1000LinkExtMvP1_P2Lst = _FlMcm1000LinkExtMvP1_P2Lst_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1, 1, 4),
    _FlMcm1000LinkExtMvP1_P2Lst_Type()
)
flMcm1000LinkExtMvP1_P2Lst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvP1_P2Lst.setStatus("current")


class _FlMcm1000LinkExtMvUpSle_Type(Integer32):
    """Custom type flMcm1000LinkExtMvUpSle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000LinkExtMvUpSle_Type.__name__ = "Integer32"
_FlMcm1000LinkExtMvUpSle_Object = MibTableColumn
flMcm1000LinkExtMvUpSle = _FlMcm1000LinkExtMvUpSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1, 1, 5),
    _FlMcm1000LinkExtMvUpSle_Type()
)
flMcm1000LinkExtMvUpSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvUpSle.setStatus("current")


class _FlMcm1000LinkExtMvDnSle_Type(Integer32):
    """Custom type flMcm1000LinkExtMvDnSle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMcm1000LinkExtMvDnSle_Type.__name__ = "Integer32"
_FlMcm1000LinkExtMvDnSle_Object = MibTableColumn
flMcm1000LinkExtMvDnSle = _FlMcm1000LinkExtMvDnSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 30, 1, 1, 6),
    _FlMcm1000LinkExtMvDnSle_Type()
)
flMcm1000LinkExtMvDnSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000LinkExtMvDnSle.setStatus("current")
flMsModuleMvChannelEntry.registerAugmentions(
    ("FIBROLAN-MIB-GBE-MCM1000",
     "flMcm1000ChannelExtMvEntry")
)
flMcm1000ChannelExtMvEntry.setIndexNames(*flMsModuleMvChannelEntry.getIndexNames())
flMsModuleMvLinkEntry.registerAugmentions(
    ("FIBROLAN-MIB-GBE-MCM1000",
     "flMcm1000LinkExtMvEntry")
)
flMcm1000LinkExtMvEntry.setIndexNames(*flMsModuleMvLinkEntry.getIndexNames())

# Managed Objects groups

flMcm1000MvChannelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 1, 2, 1)
)
flMcm1000MvChannelsGroup.setObjects(
      *(("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvP2Link"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvP1Link"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvPortDescription"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvP2SignalDetect"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvP1SignalDetect"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvChannelEnable"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvP2LoopBack"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000ChannelExtMvP1LoopBack"))
)
if mibBuilder.loadTexts:
    flMcm1000MvChannelsGroup.setStatus("current")

flMcm1000MvLinksGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 1, 2, 2)
)
flMcm1000MvLinksGroup.setObjects(
      *(("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000LinkExtMvUpstreamBw"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000LinkExtMvDownstreamBw"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000LinkExtMvP2-P1Lst"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000LinkExtMvP1-P2Lst"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000LinkExtMvUpSle"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000LinkExtMvDnSle"))
)
if mibBuilder.loadTexts:
    flMcm1000MvLinksGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMcm1000MvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 110, 1, 1, 1)
)
flMcm1000MvMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelsGroup"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinksGroup"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000MvChannelsGroup"),
        ("FIBROLAN-MIB-GBE-MCM1000", "flMcm1000MvLinksGroup"))
)
if mibBuilder.loadTexts:
    flMcm1000MvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-GBE-MCM1000",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMcm1000Mv": flMcm1000Mv,
       "flMcm1000MvMIBConformance": flMcm1000MvMIBConformance,
       "flMcm1000MvMIBCompliances": flMcm1000MvMIBCompliances,
       "flMcm1000MvMIBCompliance": flMcm1000MvMIBCompliance,
       "flMcm1000MvMIBGroups": flMcm1000MvMIBGroups,
       "flMcm1000MvChannelsGroup": flMcm1000MvChannelsGroup,
       "flMcm1000MvLinksGroup": flMcm1000MvLinksGroup,
       "flMcm1000ModuleMv": flMcm1000ModuleMv,
       "flMcm1000ChannelsMv": flMcm1000ChannelsMv,
       "flMcm1000ChannelExtMvTable": flMcm1000ChannelExtMvTable,
       "flMcm1000ChannelExtMvEntry": flMcm1000ChannelExtMvEntry,
       "flMcm1000ChannelExtMvP2Link": flMcm1000ChannelExtMvP2Link,
       "flMcm1000ChannelExtMvP1Link": flMcm1000ChannelExtMvP1Link,
       "flMcm1000ChannelExtMvPortDescription": flMcm1000ChannelExtMvPortDescription,
       "flMcm1000ChannelExtMvP2SignalDetect": flMcm1000ChannelExtMvP2SignalDetect,
       "flMcm1000ChannelExtMvP1SignalDetect": flMcm1000ChannelExtMvP1SignalDetect,
       "flMcm1000ChannelExtMvChannelEnable": flMcm1000ChannelExtMvChannelEnable,
       "flMcm1000ChannelExtMvP2LoopBack": flMcm1000ChannelExtMvP2LoopBack,
       "flMcm1000ChannelExtMvP1LoopBack": flMcm1000ChannelExtMvP1LoopBack,
       "flMcm1000LinksMv": flMcm1000LinksMv,
       "flMcm1000LinkExtMvTable": flMcm1000LinkExtMvTable,
       "flMcm1000LinkExtMvEntry": flMcm1000LinkExtMvEntry,
       "flMcm1000LinkExtMvUpstreamBw": flMcm1000LinkExtMvUpstreamBw,
       "flMcm1000LinkExtMvDownstreamBw": flMcm1000LinkExtMvDownstreamBw,
       "flMcm1000LinkExtMvP2-P1Lst": flMcm1000LinkExtMvP2_P1Lst,
       "flMcm1000LinkExtMvP1-P2Lst": flMcm1000LinkExtMvP1_P2Lst,
       "flMcm1000LinkExtMvUpSle": flMcm1000LinkExtMvUpSle,
       "flMcm1000LinkExtMvDnSle": flMcm1000LinkExtMvDnSle}
)
