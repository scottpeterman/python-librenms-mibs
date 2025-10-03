# SNMP MIB module (FIBROLAN-MIB-GBE-MCM1000X) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-GBE-MCM1000X
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:21 2025
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

flMcm1000x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150)
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
_FlMcm1000xMIBConformance_ObjectIdentity = ObjectIdentity
flMcm1000xMIBConformance = _FlMcm1000xMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 1)
)
_FlMcm1000xMIBCompliances_ObjectIdentity = ObjectIdentity
flMcm1000xMIBCompliances = _FlMcm1000xMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 1, 1)
)
_FlMcm1000xMIBGroups_ObjectIdentity = ObjectIdentity
flMcm1000xMIBGroups = _FlMcm1000xMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 1, 2)
)
_FlMcm1000xModule_ObjectIdentity = ObjectIdentity
flMcm1000xModule = _FlMcm1000xModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 10)
)
_FlMcm1000xChannels_ObjectIdentity = ObjectIdentity
flMcm1000xChannels = _FlMcm1000xChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20)
)
_FlMcm1000xChannelExtTable_Object = MibTable
flMcm1000xChannelExtTable = _FlMcm1000xChannelExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1)
)
if mibBuilder.loadTexts:
    flMcm1000xChannelExtTable.setStatus("current")
_FlMcm1000xChannelExtEntry_Object = MibTableRow
flMcm1000xChannelExtEntry = _FlMcm1000xChannelExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm1000xChannelExtEntry.setStatus("current")
_FlMcm1000xChannelExtDescription_Type = DisplayString
_FlMcm1000xChannelExtDescription_Object = MibTableColumn
flMcm1000xChannelExtDescription = _FlMcm1000xChannelExtDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 1),
    _FlMcm1000xChannelExtDescription_Type()
)
flMcm1000xChannelExtDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtDescription.setStatus("current")


class _FlMcm1000xChannelExtType_Type(Integer32):
    """Custom type flMcm1000xChannelExtType based on Integer32"""
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


_FlMcm1000xChannelExtType_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtType_Object = MibTableColumn
flMcm1000xChannelExtType = _FlMcm1000xChannelExtType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 2),
    _FlMcm1000xChannelExtType_Type()
)
flMcm1000xChannelExtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtType.setStatus("current")


class _FlMcm1000xChannelExtLink_Type(Integer32):
    """Custom type flMcm1000xChannelExtLink based on Integer32"""
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


_FlMcm1000xChannelExtLink_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtLink_Object = MibTableColumn
flMcm1000xChannelExtLink = _FlMcm1000xChannelExtLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 3),
    _FlMcm1000xChannelExtLink_Type()
)
flMcm1000xChannelExtLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtLink.setStatus("current")


class _FlMcm1000xChannelExtSignalDetect_Type(Integer32):
    """Custom type flMcm1000xChannelExtSignalDetect based on Integer32"""
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


_FlMcm1000xChannelExtSignalDetect_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtSignalDetect_Object = MibTableColumn
flMcm1000xChannelExtSignalDetect = _FlMcm1000xChannelExtSignalDetect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 4),
    _FlMcm1000xChannelExtSignalDetect_Type()
)
flMcm1000xChannelExtSignalDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtSignalDetect.setStatus("current")


class _FlMcm1000xChannelExtEnable_Type(Integer32):
    """Custom type flMcm1000xChannelExtEnable based on Integer32"""
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


_FlMcm1000xChannelExtEnable_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtEnable_Object = MibTableColumn
flMcm1000xChannelExtEnable = _FlMcm1000xChannelExtEnable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 5),
    _FlMcm1000xChannelExtEnable_Type()
)
flMcm1000xChannelExtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtEnable.setStatus("current")


class _FlMcm1000xChannelExtPause_Type(Integer32):
    """Custom type flMcm1000xChannelExtPause based on Integer32"""
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


_FlMcm1000xChannelExtPause_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtPause_Object = MibTableColumn
flMcm1000xChannelExtPause = _FlMcm1000xChannelExtPause_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 6),
    _FlMcm1000xChannelExtPause_Type()
)
flMcm1000xChannelExtPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtPause.setStatus("current")


class _FlMcm1000xChannelExtUpSle_Type(Integer32):
    """Custom type flMcm1000xChannelExtUpSle based on Integer32"""
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


_FlMcm1000xChannelExtUpSle_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtUpSle_Object = MibTableColumn
flMcm1000xChannelExtUpSle = _FlMcm1000xChannelExtUpSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 7),
    _FlMcm1000xChannelExtUpSle_Type()
)
flMcm1000xChannelExtUpSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtUpSle.setStatus("current")


class _FlMcm1000xChannelExtDownSle_Type(Integer32):
    """Custom type flMcm1000xChannelExtDownSle based on Integer32"""
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


_FlMcm1000xChannelExtDownSle_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtDownSle_Object = MibTableColumn
flMcm1000xChannelExtDownSle = _FlMcm1000xChannelExtDownSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 8),
    _FlMcm1000xChannelExtDownSle_Type()
)
flMcm1000xChannelExtDownSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtDownSle.setStatus("current")


class _FlMcm1000xChannelExtAutonego_Type(Integer32):
    """Custom type flMcm1000xChannelExtAutonego based on Integer32"""
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


_FlMcm1000xChannelExtAutonego_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtAutonego_Object = MibTableColumn
flMcm1000xChannelExtAutonego = _FlMcm1000xChannelExtAutonego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 9),
    _FlMcm1000xChannelExtAutonego_Type()
)
flMcm1000xChannelExtAutonego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtAutonego.setStatus("current")


class _FlMcm1000xChannelExtLoopBack_Type(Integer32):
    """Custom type flMcm1000xChannelExtLoopBack based on Integer32"""
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


_FlMcm1000xChannelExtLoopBack_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtLoopBack_Object = MibTableColumn
flMcm1000xChannelExtLoopBack = _FlMcm1000xChannelExtLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 10),
    _FlMcm1000xChannelExtLoopBack_Type()
)
flMcm1000xChannelExtLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtLoopBack.setStatus("current")


class _FlMcm1000xChannelExtUpstreamBw_Type(Integer32):
    """Custom type flMcm1000xChannelExtUpstreamBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FlMcm1000xChannelExtUpstreamBw_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtUpstreamBw_Object = MibTableColumn
flMcm1000xChannelExtUpstreamBw = _FlMcm1000xChannelExtUpstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 11),
    _FlMcm1000xChannelExtUpstreamBw_Type()
)
flMcm1000xChannelExtUpstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtUpstreamBw.setStatus("current")


class _FlMcm1000xChannelExtDownstreamBw_Type(Integer32):
    """Custom type flMcm1000xChannelExtDownstreamBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FlMcm1000xChannelExtDownstreamBw_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtDownstreamBw_Object = MibTableColumn
flMcm1000xChannelExtDownstreamBw = _FlMcm1000xChannelExtDownstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 12),
    _FlMcm1000xChannelExtDownstreamBw_Type()
)
flMcm1000xChannelExtDownstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtDownstreamBw.setStatus("current")


class _FlMcm1000xChannelExtP2_P1Fp_Type(Integer32):
    """Custom type flMcm1000xChannelExtP2_P1Fp based on Integer32"""
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


_FlMcm1000xChannelExtP2_P1Fp_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtP2_P1Fp_Object = MibTableColumn
flMcm1000xChannelExtP2_P1Fp = _FlMcm1000xChannelExtP2_P1Fp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 13),
    _FlMcm1000xChannelExtP2_P1Fp_Type()
)
flMcm1000xChannelExtP2_P1Fp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtP2_P1Fp.setStatus("current")


class _FlMcm1000xChannelExtP1_P2Fp_Type(Integer32):
    """Custom type flMcm1000xChannelExtP1_P2Fp based on Integer32"""
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


_FlMcm1000xChannelExtP1_P2Fp_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtP1_P2Fp_Object = MibTableColumn
flMcm1000xChannelExtP1_P2Fp = _FlMcm1000xChannelExtP1_P2Fp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 14),
    _FlMcm1000xChannelExtP1_P2Fp_Type()
)
flMcm1000xChannelExtP1_P2Fp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtP1_P2Fp.setStatus("current")


class _FlMcm1000xChannelExtP2_P1Sle_Type(Integer32):
    """Custom type flMcm1000xChannelExtP2_P1Sle based on Integer32"""
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


_FlMcm1000xChannelExtP2_P1Sle_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtP2_P1Sle_Object = MibTableColumn
flMcm1000xChannelExtP2_P1Sle = _FlMcm1000xChannelExtP2_P1Sle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 15),
    _FlMcm1000xChannelExtP2_P1Sle_Type()
)
flMcm1000xChannelExtP2_P1Sle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtP2_P1Sle.setStatus("current")


class _FlMcm1000xChannelExtP1_P2Sle_Type(Integer32):
    """Custom type flMcm1000xChannelExtP1_P2Sle based on Integer32"""
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


_FlMcm1000xChannelExtP1_P2Sle_Type.__name__ = "Integer32"
_FlMcm1000xChannelExtP1_P2Sle_Object = MibTableColumn
flMcm1000xChannelExtP1_P2Sle = _FlMcm1000xChannelExtP1_P2Sle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 20, 1, 1, 16),
    _FlMcm1000xChannelExtP1_P2Sle_Type()
)
flMcm1000xChannelExtP1_P2Sle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xChannelExtP1_P2Sle.setStatus("current")
_FlMcm1000xStatistics_ObjectIdentity = ObjectIdentity
flMcm1000xStatistics = _FlMcm1000xStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30)
)
_FlMcm1000xStatisticsTable_Object = MibTable
flMcm1000xStatisticsTable = _FlMcm1000xStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1)
)
if mibBuilder.loadTexts:
    flMcm1000xStatisticsTable.setStatus("current")
_FlMcm1000xStatisticsEntry_Object = MibTableRow
flMcm1000xStatisticsEntry = _FlMcm1000xStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm1000xStatisticsEntry.setStatus("current")
_FlMcm1000xRxDropEvents_Type = Counter64
_FlMcm1000xRxDropEvents_Object = MibTableColumn
flMcm1000xRxDropEvents = _FlMcm1000xRxDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 1),
    _FlMcm1000xRxDropEvents_Type()
)
flMcm1000xRxDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxDropEvents.setStatus("current")
_FlMcm1000xRxOctets_Type = Counter64
_FlMcm1000xRxOctets_Object = MibTableColumn
flMcm1000xRxOctets = _FlMcm1000xRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 2),
    _FlMcm1000xRxOctets_Type()
)
flMcm1000xRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxOctets.setStatus("current")
_FlMcm1000xRxPackets_Type = Counter64
_FlMcm1000xRxPackets_Object = MibTableColumn
flMcm1000xRxPackets = _FlMcm1000xRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 3),
    _FlMcm1000xRxPackets_Type()
)
flMcm1000xRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPackets.setStatus("current")
_FlMcm1000xRxBroadcastPackets_Type = Counter64
_FlMcm1000xRxBroadcastPackets_Object = MibTableColumn
flMcm1000xRxBroadcastPackets = _FlMcm1000xRxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 4),
    _FlMcm1000xRxBroadcastPackets_Type()
)
flMcm1000xRxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxBroadcastPackets.setStatus("current")
_FlMcm1000xRxMulticastPackets_Type = Counter64
_FlMcm1000xRxMulticastPackets_Object = MibTableColumn
flMcm1000xRxMulticastPackets = _FlMcm1000xRxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 5),
    _FlMcm1000xRxMulticastPackets_Type()
)
flMcm1000xRxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxMulticastPackets.setStatus("current")
_FlMcm1000xRxCrcAlignmentErrors_Type = Counter64
_FlMcm1000xRxCrcAlignmentErrors_Object = MibTableColumn
flMcm1000xRxCrcAlignmentErrors = _FlMcm1000xRxCrcAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 6),
    _FlMcm1000xRxCrcAlignmentErrors_Type()
)
flMcm1000xRxCrcAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxCrcAlignmentErrors.setStatus("current")
_FlMcm1000xRxUndersizePackets_Type = Counter64
_FlMcm1000xRxUndersizePackets_Object = MibTableColumn
flMcm1000xRxUndersizePackets = _FlMcm1000xRxUndersizePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 7),
    _FlMcm1000xRxUndersizePackets_Type()
)
flMcm1000xRxUndersizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxUndersizePackets.setStatus("current")
_FlMcm1000xRxOversizePackets_Type = Counter64
_FlMcm1000xRxOversizePackets_Object = MibTableColumn
flMcm1000xRxOversizePackets = _FlMcm1000xRxOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 8),
    _FlMcm1000xRxOversizePackets_Type()
)
flMcm1000xRxOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxOversizePackets.setStatus("current")
_FlMcm1000xRxFragments_Type = Counter64
_FlMcm1000xRxFragments_Object = MibTableColumn
flMcm1000xRxFragments = _FlMcm1000xRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 9),
    _FlMcm1000xRxFragments_Type()
)
flMcm1000xRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxFragments.setStatus("current")
_FlMcm1000xRxJabbers_Type = Counter64
_FlMcm1000xRxJabbers_Object = MibTableColumn
flMcm1000xRxJabbers = _FlMcm1000xRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 10),
    _FlMcm1000xRxJabbers_Type()
)
flMcm1000xRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxJabbers.setStatus("current")
_FlMcm1000xRxCollisions_Type = Counter64
_FlMcm1000xRxCollisions_Object = MibTableColumn
flMcm1000xRxCollisions = _FlMcm1000xRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 11),
    _FlMcm1000xRxCollisions_Type()
)
flMcm1000xRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxCollisions.setStatus("current")
_FlMcm1000xRxPackets64Octets_Type = Counter64
_FlMcm1000xRxPackets64Octets_Object = MibTableColumn
flMcm1000xRxPackets64Octets = _FlMcm1000xRxPackets64Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 12),
    _FlMcm1000xRxPackets64Octets_Type()
)
flMcm1000xRxPackets64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPackets64Octets.setStatus("current")
_FlMcm1000xRxPackets65to127Octets_Type = Counter64
_FlMcm1000xRxPackets65to127Octets_Object = MibTableColumn
flMcm1000xRxPackets65to127Octets = _FlMcm1000xRxPackets65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 13),
    _FlMcm1000xRxPackets65to127Octets_Type()
)
flMcm1000xRxPackets65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPackets65to127Octets.setStatus("current")
_FlMcm1000xRxPackets128to255Octets_Type = Counter64
_FlMcm1000xRxPackets128to255Octets_Object = MibTableColumn
flMcm1000xRxPackets128to255Octets = _FlMcm1000xRxPackets128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 14),
    _FlMcm1000xRxPackets128to255Octets_Type()
)
flMcm1000xRxPackets128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPackets128to255Octets.setStatus("current")
_FlMcm1000xRxPackets256to511Octets_Type = Counter64
_FlMcm1000xRxPackets256to511Octets_Object = MibTableColumn
flMcm1000xRxPackets256to511Octets = _FlMcm1000xRxPackets256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 15),
    _FlMcm1000xRxPackets256to511Octets_Type()
)
flMcm1000xRxPackets256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPackets256to511Octets.setStatus("current")
_FlMcm1000xRxPackets512to1023Octets_Type = Counter64
_FlMcm1000xRxPackets512to1023Octets_Object = MibTableColumn
flMcm1000xRxPackets512to1023Octets = _FlMcm1000xRxPackets512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 16),
    _FlMcm1000xRxPackets512to1023Octets_Type()
)
flMcm1000xRxPackets512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPackets512to1023Octets.setStatus("current")
_FlMcm1000xRxPackets1024toMaxOctets_Type = Counter64
_FlMcm1000xRxPackets1024toMaxOctets_Object = MibTableColumn
flMcm1000xRxPackets1024toMaxOctets = _FlMcm1000xRxPackets1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 17),
    _FlMcm1000xRxPackets1024toMaxOctets_Type()
)
flMcm1000xRxPackets1024toMaxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPackets1024toMaxOctets.setStatus("current")
_FlMcm1000xRxFibroLANProprietryFrames_Type = Counter64
_FlMcm1000xRxFibroLANProprietryFrames_Object = MibTableColumn
flMcm1000xRxFibroLANProprietryFrames = _FlMcm1000xRxFibroLANProprietryFrames_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 18),
    _FlMcm1000xRxFibroLANProprietryFrames_Type()
)
flMcm1000xRxFibroLANProprietryFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxFibroLANProprietryFrames.setStatus("current")


class _FlMcm1000xClearCounters_Type(Integer32):
    """Custom type flMcm1000xClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlMcm1000xClearCounters_Type.__name__ = "Integer32"
_FlMcm1000xClearCounters_Object = MibTableColumn
flMcm1000xClearCounters = _FlMcm1000xClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 19),
    _FlMcm1000xClearCounters_Type()
)
flMcm1000xClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1000xClearCounters.setStatus("current")
_FlMcm1000xRxOctetsRate_Type = Counter64
_FlMcm1000xRxOctetsRate_Object = MibTableColumn
flMcm1000xRxOctetsRate = _FlMcm1000xRxOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 20),
    _FlMcm1000xRxOctetsRate_Type()
)
flMcm1000xRxOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxOctetsRate.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xRxOctetsRate.setUnits("bytes/sec")
_FlMcm1000xRxBitsRate_Type = Counter64
_FlMcm1000xRxBitsRate_Object = MibTableColumn
flMcm1000xRxBitsRate = _FlMcm1000xRxBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 21),
    _FlMcm1000xRxBitsRate_Type()
)
flMcm1000xRxBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxBitsRate.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xRxBitsRate.setUnits("bits/sec")
_FlMcm1000xRxPacketsRate_Type = Counter64
_FlMcm1000xRxPacketsRate_Object = MibTableColumn
flMcm1000xRxPacketsRate = _FlMcm1000xRxPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 22),
    _FlMcm1000xRxPacketsRate_Type()
)
flMcm1000xRxPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xRxPacketsRate.setUnits("frames/sec")
_FlMcm1000xRxUtilization_Type = DisplayString
_FlMcm1000xRxUtilization_Object = MibTableColumn
flMcm1000xRxUtilization = _FlMcm1000xRxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 23),
    _FlMcm1000xRxUtilization_Type()
)
flMcm1000xRxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xRxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xRxUtilization.setUnits("%")
_FlMcm1000xTxOctets_Type = Counter64
_FlMcm1000xTxOctets_Object = MibTableColumn
flMcm1000xTxOctets = _FlMcm1000xTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 24),
    _FlMcm1000xTxOctets_Type()
)
flMcm1000xTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxOctets.setStatus("current")
_FlMcm1000xTxPackets_Type = Counter64
_FlMcm1000xTxPackets_Object = MibTableColumn
flMcm1000xTxPackets = _FlMcm1000xTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 25),
    _FlMcm1000xTxPackets_Type()
)
flMcm1000xTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxPackets.setStatus("current")
_FlMcm1000xTxBroadcastPackets_Type = Counter64
_FlMcm1000xTxBroadcastPackets_Object = MibTableColumn
flMcm1000xTxBroadcastPackets = _FlMcm1000xTxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 26),
    _FlMcm1000xTxBroadcastPackets_Type()
)
flMcm1000xTxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxBroadcastPackets.setStatus("current")
_FlMcm1000xTxMulticastPackets_Type = Counter64
_FlMcm1000xTxMulticastPackets_Object = MibTableColumn
flMcm1000xTxMulticastPackets = _FlMcm1000xTxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 27),
    _FlMcm1000xTxMulticastPackets_Type()
)
flMcm1000xTxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxMulticastPackets.setStatus("current")
_FlMcm1000xTxFibroLANProprietryFrames_Type = Counter64
_FlMcm1000xTxFibroLANProprietryFrames_Object = MibTableColumn
flMcm1000xTxFibroLANProprietryFrames = _FlMcm1000xTxFibroLANProprietryFrames_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 28),
    _FlMcm1000xTxFibroLANProprietryFrames_Type()
)
flMcm1000xTxFibroLANProprietryFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxFibroLANProprietryFrames.setStatus("current")
_FlMcm1000xTxOctetsRate_Type = Counter64
_FlMcm1000xTxOctetsRate_Object = MibTableColumn
flMcm1000xTxOctetsRate = _FlMcm1000xTxOctetsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 29),
    _FlMcm1000xTxOctetsRate_Type()
)
flMcm1000xTxOctetsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxOctetsRate.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xTxOctetsRate.setUnits("bytes/sec")
_FlMcm1000xTxBitsRate_Type = Counter64
_FlMcm1000xTxBitsRate_Object = MibTableColumn
flMcm1000xTxBitsRate = _FlMcm1000xTxBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 30),
    _FlMcm1000xTxBitsRate_Type()
)
flMcm1000xTxBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxBitsRate.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xTxBitsRate.setUnits("bits/sec")
_FlMcm1000xTxPacketsRate_Type = Counter64
_FlMcm1000xTxPacketsRate_Object = MibTableColumn
flMcm1000xTxPacketsRate = _FlMcm1000xTxPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 31),
    _FlMcm1000xTxPacketsRate_Type()
)
flMcm1000xTxPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxPacketsRate.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xTxPacketsRate.setUnits("frames/sec")
_FlMcm1000xTxUtilization_Type = DisplayString
_FlMcm1000xTxUtilization_Object = MibTableColumn
flMcm1000xTxUtilization = _FlMcm1000xTxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 30, 1, 1, 32),
    _FlMcm1000xTxUtilization_Type()
)
flMcm1000xTxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1000xTxUtilization.setStatus("current")
if mibBuilder.loadTexts:
    flMcm1000xTxUtilization.setUnits("%")
flMsModuleMvChannelEntry.registerAugmentions(
    ("FIBROLAN-MIB-GBE-MCM1000X",
     "flMcm1000xChannelExtEntry")
)
flMcm1000xChannelExtEntry.setIndexNames(*flMsModuleMvChannelEntry.getIndexNames())
flMsModuleMvChannelEntry.registerAugmentions(
    ("FIBROLAN-MIB-GBE-MCM1000X",
     "flMcm1000xStatisticsEntry")
)
flMcm1000xStatisticsEntry.setIndexNames(*flMsModuleMvChannelEntry.getIndexNames())

# Managed Objects groups

flMcm1000xChannelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 1, 2, 1)
)
flMcm1000xChannelsGroup.setObjects(
      *(("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtDescription"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtType"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtLink"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtSignalDetect"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtEnable"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtPause"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtUpSle"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtDownSle"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtAutonego"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtLoopBack"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtUpstreamBw"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtDownstreamBw"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtP2-P1Fp"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtP1-P2Fp"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtP2-P1Sle"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelExtP1-P2Sle"))
)
if mibBuilder.loadTexts:
    flMcm1000xChannelsGroup.setStatus("current")

flMcm1000xStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 1, 2, 2)
)
flMcm1000xStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxDropEvents"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxOctets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxBroadcastPackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxMulticastPackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxCrcAlignmentErrors"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxUndersizePackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxOversizePackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxFragments"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxJabbers"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxCollisions"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPackets64Octets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPackets65to127Octets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPackets128to255Octets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPackets256to511Octets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPackets512to1023Octets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPackets1024toMaxOctets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxFibroLANProprietryFrames"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xClearCounters"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxOctetsRate"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxBitsRate"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxPacketsRate"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xRxUtilization"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxOctets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxPackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxBroadcastPackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxMulticastPackets"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxFibroLANProprietryFrames"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxOctetsRate"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxBitsRate"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxPacketsRate"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xTxUtilization"))
)
if mibBuilder.loadTexts:
    flMcm1000xStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMcm1000xMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 150, 1, 1, 1)
)
flMcm1000xMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelsGroup"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xChannelsGroup"),
        ("FIBROLAN-MIB-GBE-MCM1000X", "flMcm1000xStatisticsGroup"))
)
if mibBuilder.loadTexts:
    flMcm1000xMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-GBE-MCM1000X",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMcm1000x": flMcm1000x,
       "flMcm1000xMIBConformance": flMcm1000xMIBConformance,
       "flMcm1000xMIBCompliances": flMcm1000xMIBCompliances,
       "flMcm1000xMIBCompliance": flMcm1000xMIBCompliance,
       "flMcm1000xMIBGroups": flMcm1000xMIBGroups,
       "flMcm1000xChannelsGroup": flMcm1000xChannelsGroup,
       "flMcm1000xStatisticsGroup": flMcm1000xStatisticsGroup,
       "flMcm1000xModule": flMcm1000xModule,
       "flMcm1000xChannels": flMcm1000xChannels,
       "flMcm1000xChannelExtTable": flMcm1000xChannelExtTable,
       "flMcm1000xChannelExtEntry": flMcm1000xChannelExtEntry,
       "flMcm1000xChannelExtDescription": flMcm1000xChannelExtDescription,
       "flMcm1000xChannelExtType": flMcm1000xChannelExtType,
       "flMcm1000xChannelExtLink": flMcm1000xChannelExtLink,
       "flMcm1000xChannelExtSignalDetect": flMcm1000xChannelExtSignalDetect,
       "flMcm1000xChannelExtEnable": flMcm1000xChannelExtEnable,
       "flMcm1000xChannelExtPause": flMcm1000xChannelExtPause,
       "flMcm1000xChannelExtUpSle": flMcm1000xChannelExtUpSle,
       "flMcm1000xChannelExtDownSle": flMcm1000xChannelExtDownSle,
       "flMcm1000xChannelExtAutonego": flMcm1000xChannelExtAutonego,
       "flMcm1000xChannelExtLoopBack": flMcm1000xChannelExtLoopBack,
       "flMcm1000xChannelExtUpstreamBw": flMcm1000xChannelExtUpstreamBw,
       "flMcm1000xChannelExtDownstreamBw": flMcm1000xChannelExtDownstreamBw,
       "flMcm1000xChannelExtP2-P1Fp": flMcm1000xChannelExtP2_P1Fp,
       "flMcm1000xChannelExtP1-P2Fp": flMcm1000xChannelExtP1_P2Fp,
       "flMcm1000xChannelExtP2-P1Sle": flMcm1000xChannelExtP2_P1Sle,
       "flMcm1000xChannelExtP1-P2Sle": flMcm1000xChannelExtP1_P2Sle,
       "flMcm1000xStatistics": flMcm1000xStatistics,
       "flMcm1000xStatisticsTable": flMcm1000xStatisticsTable,
       "flMcm1000xStatisticsEntry": flMcm1000xStatisticsEntry,
       "flMcm1000xRxDropEvents": flMcm1000xRxDropEvents,
       "flMcm1000xRxOctets": flMcm1000xRxOctets,
       "flMcm1000xRxPackets": flMcm1000xRxPackets,
       "flMcm1000xRxBroadcastPackets": flMcm1000xRxBroadcastPackets,
       "flMcm1000xRxMulticastPackets": flMcm1000xRxMulticastPackets,
       "flMcm1000xRxCrcAlignmentErrors": flMcm1000xRxCrcAlignmentErrors,
       "flMcm1000xRxUndersizePackets": flMcm1000xRxUndersizePackets,
       "flMcm1000xRxOversizePackets": flMcm1000xRxOversizePackets,
       "flMcm1000xRxFragments": flMcm1000xRxFragments,
       "flMcm1000xRxJabbers": flMcm1000xRxJabbers,
       "flMcm1000xRxCollisions": flMcm1000xRxCollisions,
       "flMcm1000xRxPackets64Octets": flMcm1000xRxPackets64Octets,
       "flMcm1000xRxPackets65to127Octets": flMcm1000xRxPackets65to127Octets,
       "flMcm1000xRxPackets128to255Octets": flMcm1000xRxPackets128to255Octets,
       "flMcm1000xRxPackets256to511Octets": flMcm1000xRxPackets256to511Octets,
       "flMcm1000xRxPackets512to1023Octets": flMcm1000xRxPackets512to1023Octets,
       "flMcm1000xRxPackets1024toMaxOctets": flMcm1000xRxPackets1024toMaxOctets,
       "flMcm1000xRxFibroLANProprietryFrames": flMcm1000xRxFibroLANProprietryFrames,
       "flMcm1000xClearCounters": flMcm1000xClearCounters,
       "flMcm1000xRxOctetsRate": flMcm1000xRxOctetsRate,
       "flMcm1000xRxBitsRate": flMcm1000xRxBitsRate,
       "flMcm1000xRxPacketsRate": flMcm1000xRxPacketsRate,
       "flMcm1000xRxUtilization": flMcm1000xRxUtilization,
       "flMcm1000xTxOctets": flMcm1000xTxOctets,
       "flMcm1000xTxPackets": flMcm1000xTxPackets,
       "flMcm1000xTxBroadcastPackets": flMcm1000xTxBroadcastPackets,
       "flMcm1000xTxMulticastPackets": flMcm1000xTxMulticastPackets,
       "flMcm1000xTxFibroLANProprietryFrames": flMcm1000xTxFibroLANProprietryFrames,
       "flMcm1000xTxOctetsRate": flMcm1000xTxOctetsRate,
       "flMcm1000xTxBitsRate": flMcm1000xTxBitsRate,
       "flMcm1000xTxPacketsRate": flMcm1000xTxPacketsRate,
       "flMcm1000xTxUtilization": flMcm1000xTxUtilization}
)
