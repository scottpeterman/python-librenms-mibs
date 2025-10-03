# SNMP MIB module (FIBROLAN-MIB-GBE-MCM1000XRL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-GBE-MCM1000XRL
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:22 2025
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

(flMsChassisModuleMvIndex,
 flMsChassisMvIndex) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    "flMsChassisModuleMvIndex",
    "flMsChassisMvIndex")

(flMsModuleMvChannelEntry,) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-MSMODULE",
    "flMsModuleMvChannelEntry")

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

flMcm1000xrl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170)
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
_FlMcm1000xrlMIBConformance_ObjectIdentity = ObjectIdentity
flMcm1000xrlMIBConformance = _FlMcm1000xrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 1)
)
_FlMcm1000xrlMIBCompliances_ObjectIdentity = ObjectIdentity
flMcm1000xrlMIBCompliances = _FlMcm1000xrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 1, 1)
)
_FlMcm1000xrlMIBGroups_ObjectIdentity = ObjectIdentity
flMcm1000xrlMIBGroups = _FlMcm1000xrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 1, 2)
)
_FlMcm1000xrlModule_ObjectIdentity = ObjectIdentity
flMcm1000xrlModule = _FlMcm1000xrlModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10)
)
_FlMcm1000xrlModuleTable_Object = MibTable
flMcm1000xrlModuleTable = _FlMcm1000xrlModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1)
)
if mibBuilder.loadTexts:
    flMcm1000xrlModuleTable.setStatus("current")
_FlMcm1000xrlModuleEntry_Object = MibTableRow
flMcm1000xrlModuleEntry = _FlMcm1000xrlModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1)
)
flMcm1000xrlModuleEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
)
if mibBuilder.loadTexts:
    flMcm1000xrlModuleEntry.setStatus("current")


class _FlMcm1000xrlModuleRedundantMode_Type(Integer32):
    """Custom type flMcm1000xrlModuleRedundantMode based on Integer32"""
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


_FlMcm1000xrlModuleRedundantMode_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleRedundantMode_Object = MibTableColumn
flMcm1000xrlModuleRedundantMode = _FlMcm1000xrlModuleRedundantMode_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 1),
    _FlMcm1000xrlModuleRedundantMode_Type()
)
flMcm1000xrlModuleRedundantMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleRedundantMode.setStatus("current")


class _FlMcm1000xrlModuleBckp2MainTimeLocal_Type(Integer32):
    """Custom type flMcm1000xrlModuleBckp2MainTimeLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sec0", 1),
          ("sec1", 2),
          ("sec5", 3),
          ("sec10", 4),
          ("sec20", 5),
          ("never", 7))
    )


_FlMcm1000xrlModuleBckp2MainTimeLocal_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleBckp2MainTimeLocal_Object = MibTableColumn
flMcm1000xrlModuleBckp2MainTimeLocal = _FlMcm1000xrlModuleBckp2MainTimeLocal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 2),
    _FlMcm1000xrlModuleBckp2MainTimeLocal_Type()
)
flMcm1000xrlModuleBckp2MainTimeLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleBckp2MainTimeLocal.setStatus("current")


class _FlMcm1000xrlModuleBckp2MainTimeRemote_Type(Integer32):
    """Custom type flMcm1000xrlModuleBckp2MainTimeRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sec0", 1),
          ("sec1", 2),
          ("sec5", 3),
          ("sec10", 4),
          ("sec20", 5),
          ("never", 7))
    )


_FlMcm1000xrlModuleBckp2MainTimeRemote_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleBckp2MainTimeRemote_Object = MibTableColumn
flMcm1000xrlModuleBckp2MainTimeRemote = _FlMcm1000xrlModuleBckp2MainTimeRemote_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 3),
    _FlMcm1000xrlModuleBckp2MainTimeRemote_Type()
)
flMcm1000xrlModuleBckp2MainTimeRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleBckp2MainTimeRemote.setStatus("current")


class _FlMcm1000xrlModuleForceBckpLocal_Type(Integer32):
    """Custom type flMcm1000xrlModuleForceBckpLocal based on Integer32"""
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


_FlMcm1000xrlModuleForceBckpLocal_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleForceBckpLocal_Object = MibTableColumn
flMcm1000xrlModuleForceBckpLocal = _FlMcm1000xrlModuleForceBckpLocal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 4),
    _FlMcm1000xrlModuleForceBckpLocal_Type()
)
flMcm1000xrlModuleForceBckpLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleForceBckpLocal.setStatus("current")


class _FlMcm1000xrlModuleForceBckpRemote_Type(Integer32):
    """Custom type flMcm1000xrlModuleForceBckpRemote based on Integer32"""
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


_FlMcm1000xrlModuleForceBckpRemote_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleForceBckpRemote_Object = MibTableColumn
flMcm1000xrlModuleForceBckpRemote = _FlMcm1000xrlModuleForceBckpRemote_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 5),
    _FlMcm1000xrlModuleForceBckpRemote_Type()
)
flMcm1000xrlModuleForceBckpRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleForceBckpRemote.setStatus("current")


class _FlMcm1000xrlModuleBckpUnusedLocal_Type(Integer32):
    """Custom type flMcm1000xrlModuleBckpUnusedLocal based on Integer32"""
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


_FlMcm1000xrlModuleBckpUnusedLocal_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleBckpUnusedLocal_Object = MibTableColumn
flMcm1000xrlModuleBckpUnusedLocal = _FlMcm1000xrlModuleBckpUnusedLocal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 6),
    _FlMcm1000xrlModuleBckpUnusedLocal_Type()
)
flMcm1000xrlModuleBckpUnusedLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleBckpUnusedLocal.setStatus("current")


class _FlMcm1000xrlModuleBckpUnusedRemote_Type(Integer32):
    """Custom type flMcm1000xrlModuleBckpUnusedRemote based on Integer32"""
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


_FlMcm1000xrlModuleBckpUnusedRemote_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleBckpUnusedRemote_Object = MibTableColumn
flMcm1000xrlModuleBckpUnusedRemote = _FlMcm1000xrlModuleBckpUnusedRemote_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 7),
    _FlMcm1000xrlModuleBckpUnusedRemote_Type()
)
flMcm1000xrlModuleBckpUnusedRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleBckpUnusedRemote.setStatus("current")


class _FlMcm1000xrlModuleRedundancySle_Type(Integer32):
    """Custom type flMcm1000xrlModuleRedundancySle based on Integer32"""
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


_FlMcm1000xrlModuleRedundancySle_Type.__name__ = "Integer32"
_FlMcm1000xrlModuleRedundancySle_Object = MibTableColumn
flMcm1000xrlModuleRedundancySle = _FlMcm1000xrlModuleRedundancySle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 10, 1, 1, 8),
    _FlMcm1000xrlModuleRedundancySle_Type()
)
flMcm1000xrlModuleRedundancySle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlModuleRedundancySle.setStatus("current")
_FlMcm1000xrlChannels_ObjectIdentity = ObjectIdentity
flMcm1000xrlChannels = _FlMcm1000xrlChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20)
)
_FlMcm1000xrlChannelTable_Object = MibTable
flMcm1000xrlChannelTable = _FlMcm1000xrlChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1)
)
if mibBuilder.loadTexts:
    flMcm1000xrlChannelTable.setStatus("current")
_FlMcm1000xrlChannelEntry_Object = MibTableRow
flMcm1000xrlChannelEntry = _FlMcm1000xrlChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1)
)
flMcm1000xrlChannelEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelType"),
)
if mibBuilder.loadTexts:
    flMcm1000xrlChannelEntry.setStatus("current")


class _FlMcm1000xrlChannelType_Type(Integer32):
    """Custom type flMcm1000xrlChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("backup", 2))
    )


_FlMcm1000xrlChannelType_Type.__name__ = "Integer32"
_FlMcm1000xrlChannelType_Object = MibTableColumn
flMcm1000xrlChannelType = _FlMcm1000xrlChannelType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 1),
    _FlMcm1000xrlChannelType_Type()
)
flMcm1000xrlChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelType.setStatus("current")
_FlMcm1000xrlChannelDescription_Type = DisplayString
_FlMcm1000xrlChannelDescription_Object = MibTableColumn
flMcm1000xrlChannelDescription = _FlMcm1000xrlChannelDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 2),
    _FlMcm1000xrlChannelDescription_Type()
)
flMcm1000xrlChannelDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelDescription.setStatus("current")


class _FlMcm1000xrlChannelUpSle_Type(Integer32):
    """Custom type flMcm1000xrlChannelUpSle based on Integer32"""
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


_FlMcm1000xrlChannelUpSle_Type.__name__ = "Integer32"
_FlMcm1000xrlChannelUpSle_Object = MibTableColumn
flMcm1000xrlChannelUpSle = _FlMcm1000xrlChannelUpSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 3),
    _FlMcm1000xrlChannelUpSle_Type()
)
flMcm1000xrlChannelUpSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelUpSle.setStatus("current")


class _FlMcm1000xrlChannelDownSle_Type(Integer32):
    """Custom type flMcm1000xrlChannelDownSle based on Integer32"""
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


_FlMcm1000xrlChannelDownSle_Type.__name__ = "Integer32"
_FlMcm1000xrlChannelDownSle_Object = MibTableColumn
flMcm1000xrlChannelDownSle = _FlMcm1000xrlChannelDownSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 4),
    _FlMcm1000xrlChannelDownSle_Type()
)
flMcm1000xrlChannelDownSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelDownSle.setStatus("current")


class _FlMcm1000xrlChannelUpstreamBw_Type(Integer32):
    """Custom type flMcm1000xrlChannelUpstreamBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FlMcm1000xrlChannelUpstreamBw_Type.__name__ = "Integer32"
_FlMcm1000xrlChannelUpstreamBw_Object = MibTableColumn
flMcm1000xrlChannelUpstreamBw = _FlMcm1000xrlChannelUpstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 5),
    _FlMcm1000xrlChannelUpstreamBw_Type()
)
flMcm1000xrlChannelUpstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelUpstreamBw.setStatus("current")


class _FlMcm1000xrlChannelDownstreamBw_Type(Integer32):
    """Custom type flMcm1000xrlChannelDownstreamBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FlMcm1000xrlChannelDownstreamBw_Type.__name__ = "Integer32"
_FlMcm1000xrlChannelDownstreamBw_Object = MibTableColumn
flMcm1000xrlChannelDownstreamBw = _FlMcm1000xrlChannelDownstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 6),
    _FlMcm1000xrlChannelDownstreamBw_Type()
)
flMcm1000xrlChannelDownstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelDownstreamBw.setStatus("current")


class _FlMcm1000xrlChannelP2_P1Fp_Type(Integer32):
    """Custom type flMcm1000xrlChannelP2_P1Fp based on Integer32"""
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


_FlMcm1000xrlChannelP2_P1Fp_Type.__name__ = "Integer32"
_FlMcm1000xrlChannelP2_P1Fp_Object = MibTableColumn
flMcm1000xrlChannelP2_P1Fp = _FlMcm1000xrlChannelP2_P1Fp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 7),
    _FlMcm1000xrlChannelP2_P1Fp_Type()
)
flMcm1000xrlChannelP2_P1Fp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelP2_P1Fp.setStatus("current")


class _FlMcm1000xrlChannelP1_P2Fp_Type(Integer32):
    """Custom type flMcm1000xrlChannelP1_P2Fp based on Integer32"""
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


_FlMcm1000xrlChannelP1_P2Fp_Type.__name__ = "Integer32"
_FlMcm1000xrlChannelP1_P2Fp_Object = MibTableColumn
flMcm1000xrlChannelP1_P2Fp = _FlMcm1000xrlChannelP1_P2Fp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 20, 1, 1, 8),
    _FlMcm1000xrlChannelP1_P2Fp_Type()
)
flMcm1000xrlChannelP1_P2Fp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlChannelP1_P2Fp.setStatus("current")
_FlMcm1000xrlPorts_ObjectIdentity = ObjectIdentity
flMcm1000xrlPorts = _FlMcm1000xrlPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30)
)
_FlMcm1000xrlPortTable_Object = MibTable
flMcm1000xrlPortTable = _FlMcm1000xrlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1)
)
if mibBuilder.loadTexts:
    flMcm1000xrlPortTable.setStatus("current")
_FlMcm1000xrlPortEntry_Object = MibTableRow
flMcm1000xrlPortEntry = _FlMcm1000xrlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1)
)
flMcm1000xrlPortEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelType"),
    (0, "FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortIndex"),
)
if mibBuilder.loadTexts:
    flMcm1000xrlPortEntry.setStatus("current")


class _FlMcm1000xrlPortIndex_Type(Integer32):
    """Custom type flMcm1000xrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlMcm1000xrlPortIndex_Type.__name__ = "Integer32"
_FlMcm1000xrlPortIndex_Object = MibTableColumn
flMcm1000xrlPortIndex = _FlMcm1000xrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 1),
    _FlMcm1000xrlPortIndex_Type()
)
flMcm1000xrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xrlPortIndex.setStatus("current")


class _FlMcm1000xrlPortType_Type(Integer32):
    """Custom type flMcm1000xrlPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tp", 1),
          ("fo", 2),
          ("n-a", 3))
    )


_FlMcm1000xrlPortType_Type.__name__ = "Integer32"
_FlMcm1000xrlPortType_Object = MibTableColumn
flMcm1000xrlPortType = _FlMcm1000xrlPortType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 2),
    _FlMcm1000xrlPortType_Type()
)
flMcm1000xrlPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xrlPortType.setStatus("current")


class _FlMcm1000xrlPortLink_Type(Integer32):
    """Custom type flMcm1000xrlPortLink based on Integer32"""
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
          ("kld", 3))
    )


_FlMcm1000xrlPortLink_Type.__name__ = "Integer32"
_FlMcm1000xrlPortLink_Object = MibTableColumn
flMcm1000xrlPortLink = _FlMcm1000xrlPortLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 3),
    _FlMcm1000xrlPortLink_Type()
)
flMcm1000xrlPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xrlPortLink.setStatus("current")


class _FlMcm1000xrlPortSignalDetect_Type(Integer32):
    """Custom type flMcm1000xrlPortSignalDetect based on Integer32"""
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


_FlMcm1000xrlPortSignalDetect_Type.__name__ = "Integer32"
_FlMcm1000xrlPortSignalDetect_Object = MibTableColumn
flMcm1000xrlPortSignalDetect = _FlMcm1000xrlPortSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 4),
    _FlMcm1000xrlPortSignalDetect_Type()
)
flMcm1000xrlPortSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xrlPortSignalDetect.setStatus("current")


class _FlMcm1000xrlPortState_Type(Integer32):
    """Custom type flMcm1000xrlPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("unused", 3),
          ("down", 4),
          ("not-applicable", 5))
    )


_FlMcm1000xrlPortState_Type.__name__ = "Integer32"
_FlMcm1000xrlPortState_Object = MibTableColumn
flMcm1000xrlPortState = _FlMcm1000xrlPortState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 5),
    _FlMcm1000xrlPortState_Type()
)
flMcm1000xrlPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xrlPortState.setStatus("current")


class _FlMcm1000xrlPortEnable_Type(Integer32):
    """Custom type flMcm1000xrlPortEnable based on Integer32"""
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


_FlMcm1000xrlPortEnable_Type.__name__ = "Integer32"
_FlMcm1000xrlPortEnable_Object = MibTableColumn
flMcm1000xrlPortEnable = _FlMcm1000xrlPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 6),
    _FlMcm1000xrlPortEnable_Type()
)
flMcm1000xrlPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlPortEnable.setStatus("current")


class _FlMcm1000xrlPortAutoNego_Type(Integer32):
    """Custom type flMcm1000xrlPortAutoNego based on Integer32"""
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


_FlMcm1000xrlPortAutoNego_Type.__name__ = "Integer32"
_FlMcm1000xrlPortAutoNego_Object = MibTableColumn
flMcm1000xrlPortAutoNego = _FlMcm1000xrlPortAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 7),
    _FlMcm1000xrlPortAutoNego_Type()
)
flMcm1000xrlPortAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlPortAutoNego.setStatus("current")


class _FlMcm1000xrlPortPause_Type(Integer32):
    """Custom type flMcm1000xrlPortPause based on Integer32"""
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


_FlMcm1000xrlPortPause_Type.__name__ = "Integer32"
_FlMcm1000xrlPortPause_Object = MibTableColumn
flMcm1000xrlPortPause = _FlMcm1000xrlPortPause_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 8),
    _FlMcm1000xrlPortPause_Type()
)
flMcm1000xrlPortPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlPortPause.setStatus("current")


class _FlMcm1000xrlPortLb_Type(Integer32):
    """Custom type flMcm1000xrlPortLb based on Integer32"""
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


_FlMcm1000xrlPortLb_Type.__name__ = "Integer32"
_FlMcm1000xrlPortLb_Object = MibTableColumn
flMcm1000xrlPortLb = _FlMcm1000xrlPortLb_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 30, 1, 1, 9),
    _FlMcm1000xrlPortLb_Type()
)
flMcm1000xrlPortLb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xrlPortLb.setStatus("current")

# Managed Objects groups

flMcm1000xrlModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 1, 2, 1)
)
flMcm1000xrlModuleGroup.setObjects(
      *(("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleRedundantMode"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleBckp2MainTimeLocal"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleBckp2MainTimeRemote"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleForceBckpLocal"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleForceBckpRemote"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleBckpUnusedLocal"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleBckpUnusedRemote"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleRedundancySle"))
)
if mibBuilder.loadTexts:
    flMcm1000xrlModuleGroup.setStatus("current")

flMcm1000xrlChannelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 1, 2, 2)
)
flMcm1000xrlChannelsGroup.setObjects(
      *(("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelType"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelDescription"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelUpSle"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelDownSle"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelUpstreamBw"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelDownstreamBw"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelP2-P1Fp"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelP1-P2Fp"))
)
if mibBuilder.loadTexts:
    flMcm1000xrlChannelsGroup.setStatus("current")

flMcm1000xrlPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 1, 2, 3)
)
flMcm1000xrlPortsGroup.setObjects(
      *(("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortIndex"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortType"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortLink"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortSignalDetect"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortState"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortEnable"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortAutoNego"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortPause"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortLb"))
)
if mibBuilder.loadTexts:
    flMcm1000xrlPortsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMcm1000xrlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 170, 1, 1, 1)
)
flMcm1000xrlMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelsGroup"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlModuleGroup"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlChannelsGroup"),
        ("FIBROLAN-MIB-GBE-MCM1000XRL", "flMcm1000xrlPortsGroup"))
)
if mibBuilder.loadTexts:
    flMcm1000xrlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-GBE-MCM1000XRL",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMcm1000xrl": flMcm1000xrl,
       "flMcm1000xrlMIBConformance": flMcm1000xrlMIBConformance,
       "flMcm1000xrlMIBCompliances": flMcm1000xrlMIBCompliances,
       "flMcm1000xrlMIBCompliance": flMcm1000xrlMIBCompliance,
       "flMcm1000xrlMIBGroups": flMcm1000xrlMIBGroups,
       "flMcm1000xrlModuleGroup": flMcm1000xrlModuleGroup,
       "flMcm1000xrlChannelsGroup": flMcm1000xrlChannelsGroup,
       "flMcm1000xrlPortsGroup": flMcm1000xrlPortsGroup,
       "flMcm1000xrlModule": flMcm1000xrlModule,
       "flMcm1000xrlModuleTable": flMcm1000xrlModuleTable,
       "flMcm1000xrlModuleEntry": flMcm1000xrlModuleEntry,
       "flMcm1000xrlModuleRedundantMode": flMcm1000xrlModuleRedundantMode,
       "flMcm1000xrlModuleBckp2MainTimeLocal": flMcm1000xrlModuleBckp2MainTimeLocal,
       "flMcm1000xrlModuleBckp2MainTimeRemote": flMcm1000xrlModuleBckp2MainTimeRemote,
       "flMcm1000xrlModuleForceBckpLocal": flMcm1000xrlModuleForceBckpLocal,
       "flMcm1000xrlModuleForceBckpRemote": flMcm1000xrlModuleForceBckpRemote,
       "flMcm1000xrlModuleBckpUnusedLocal": flMcm1000xrlModuleBckpUnusedLocal,
       "flMcm1000xrlModuleBckpUnusedRemote": flMcm1000xrlModuleBckpUnusedRemote,
       "flMcm1000xrlModuleRedundancySle": flMcm1000xrlModuleRedundancySle,
       "flMcm1000xrlChannels": flMcm1000xrlChannels,
       "flMcm1000xrlChannelTable": flMcm1000xrlChannelTable,
       "flMcm1000xrlChannelEntry": flMcm1000xrlChannelEntry,
       "flMcm1000xrlChannelType": flMcm1000xrlChannelType,
       "flMcm1000xrlChannelDescription": flMcm1000xrlChannelDescription,
       "flMcm1000xrlChannelUpSle": flMcm1000xrlChannelUpSle,
       "flMcm1000xrlChannelDownSle": flMcm1000xrlChannelDownSle,
       "flMcm1000xrlChannelUpstreamBw": flMcm1000xrlChannelUpstreamBw,
       "flMcm1000xrlChannelDownstreamBw": flMcm1000xrlChannelDownstreamBw,
       "flMcm1000xrlChannelP2-P1Fp": flMcm1000xrlChannelP2_P1Fp,
       "flMcm1000xrlChannelP1-P2Fp": flMcm1000xrlChannelP1_P2Fp,
       "flMcm1000xrlPorts": flMcm1000xrlPorts,
       "flMcm1000xrlPortTable": flMcm1000xrlPortTable,
       "flMcm1000xrlPortEntry": flMcm1000xrlPortEntry,
       "flMcm1000xrlPortIndex": flMcm1000xrlPortIndex,
       "flMcm1000xrlPortType": flMcm1000xrlPortType,
       "flMcm1000xrlPortLink": flMcm1000xrlPortLink,
       "flMcm1000xrlPortSignalDetect": flMcm1000xrlPortSignalDetect,
       "flMcm1000xrlPortState": flMcm1000xrlPortState,
       "flMcm1000xrlPortEnable": flMcm1000xrlPortEnable,
       "flMcm1000xrlPortAutoNego": flMcm1000xrlPortAutoNego,
       "flMcm1000xrlPortPause": flMcm1000xrlPortPause,
       "flMcm1000xrlPortLb": flMcm1000xrlPortLb}
)
