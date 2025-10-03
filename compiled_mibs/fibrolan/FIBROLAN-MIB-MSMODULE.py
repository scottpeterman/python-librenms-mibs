# SNMP MIB module (FIBROLAN-MIB-MSMODULE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-MSMODULE
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

(flMsChassisModuleMvIndex,
 flMsChassisMvIndex) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    "flMsChassisModuleMvIndex",
    "flMsChassisMvIndex")

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

flMsModuleMv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30)
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
_FlMsModuleMIBConformance_ObjectIdentity = ObjectIdentity
flMsModuleMIBConformance = _FlMsModuleMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 1)
)
_FlMsModuleMIBCompliances_ObjectIdentity = ObjectIdentity
flMsModuleMIBCompliances = _FlMsModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 1, 1)
)
_FlMsModuleMIBGroups_ObjectIdentity = ObjectIdentity
flMsModuleMIBGroups = _FlMsModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 1, 2)
)
_FlMsModuleChannelsMv_ObjectIdentity = ObjectIdentity
flMsModuleChannelsMv = _FlMsModuleChannelsMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 10)
)
_FlMsModuleMvChannelTable_Object = MibTable
flMsModuleMvChannelTable = _FlMsModuleMvChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 10, 1)
)
if mibBuilder.loadTexts:
    flMsModuleMvChannelTable.setStatus("current")
_FlMsModuleMvChannelEntry_Object = MibTableRow
flMsModuleMvChannelEntry = _FlMsModuleMvChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 10, 1, 1)
)
flMsModuleMvChannelEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex"),
)
if mibBuilder.loadTexts:
    flMsModuleMvChannelEntry.setStatus("current")


class _FlMsModuleMvChannelIndex_Type(Integer32):
    """Custom type flMsModuleMvChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FlMsModuleMvChannelIndex_Type.__name__ = "Integer32"
_FlMsModuleMvChannelIndex_Object = MibTableColumn
flMsModuleMvChannelIndex = _FlMsModuleMvChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 10, 1, 1, 1),
    _FlMsModuleMvChannelIndex_Type()
)
flMsModuleMvChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvChannelIndex.setStatus("current")
_FlMsModuleLinksMv_ObjectIdentity = ObjectIdentity
flMsModuleLinksMv = _FlMsModuleLinksMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20)
)
_FlMsModuleMvLinkTable_Object = MibTable
flMsModuleMvLinkTable = _FlMsModuleMvLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1)
)
if mibBuilder.loadTexts:
    flMsModuleMvLinkTable.setStatus("current")
_FlMsModuleMvLinkEntry_Object = MibTableRow
flMsModuleMvLinkEntry = _FlMsModuleMvLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1)
)
flMsModuleMvLinkEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkIndex"),
)
if mibBuilder.loadTexts:
    flMsModuleMvLinkEntry.setStatus("current")


class _FlMsModuleMvLinkIndex_Type(Integer32):
    """Custom type flMsModuleMvLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FlMsModuleMvLinkIndex_Type.__name__ = "Integer32"
_FlMsModuleMvLinkIndex_Object = MibTableColumn
flMsModuleMvLinkIndex = _FlMsModuleMvLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 1),
    _FlMsModuleMvLinkIndex_Type()
)
flMsModuleMvLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkIndex.setStatus("current")


class _FlMsModuleMvLinkRemoteDevice_Type(Integer32):
    """Custom type flMsModuleMvLinkRemoteDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("hcon-ma", 1),
          ("scon1ma", 2),
          ("fcon1ma", 3),
          ("lta41ma", 4),
          ("gsm1000ma", 5),
          ("gsm1010ma", 6),
          ("lta41-1e1", 7),
          ("lta41-2e1", 8),
          ("atara100", 9),
          ("atara1000", 10),
          ("fcon1f", 11),
          ("atara1000rm", 12),
          ("gsm1000x", 13),
          ("lta41-1t1", 14),
          ("lta41-2t1", 15),
          ("lta41-4e1", 16),
          ("lta41-4t1", 17),
          ("none-ma-attached", 9999))
    )


_FlMsModuleMvLinkRemoteDevice_Type.__name__ = "Integer32"
_FlMsModuleMvLinkRemoteDevice_Object = MibTableColumn
flMsModuleMvLinkRemoteDevice = _FlMsModuleMvLinkRemoteDevice_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 2),
    _FlMsModuleMvLinkRemoteDevice_Type()
)
flMsModuleMvLinkRemoteDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRemoteDevice.setStatus("current")


class _FlMsModuleMvLinkRemoteState_Type(Integer32):
    """Custom type flMsModuleMvLinkRemoteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ok", 2),
          ("powerFail", 3))
    )


_FlMsModuleMvLinkRemoteState_Type.__name__ = "Integer32"
_FlMsModuleMvLinkRemoteState_Object = MibTableColumn
flMsModuleMvLinkRemoteState = _FlMsModuleMvLinkRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 3),
    _FlMsModuleMvLinkRemoteState_Type()
)
flMsModuleMvLinkRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRemoteState.setStatus("current")


class _FlMsModuleMvLinkRestoreDefaults_Type(Integer32):
    """Custom type flMsModuleMvLinkRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("restore", 2))
    )


_FlMsModuleMvLinkRestoreDefaults_Type.__name__ = "Integer32"
_FlMsModuleMvLinkRestoreDefaults_Object = MibTableColumn
flMsModuleMvLinkRestoreDefaults = _FlMsModuleMvLinkRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 4),
    _FlMsModuleMvLinkRestoreDefaults_Type()
)
flMsModuleMvLinkRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRestoreDefaults.setStatus("current")
_FlMsModuleMvLinkRemoteSerialNumber_Type = DisplayString
_FlMsModuleMvLinkRemoteSerialNumber_Object = MibTableColumn
flMsModuleMvLinkRemoteSerialNumber = _FlMsModuleMvLinkRemoteSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 5),
    _FlMsModuleMvLinkRemoteSerialNumber_Type()
)
flMsModuleMvLinkRemoteSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRemoteSerialNumber.setStatus("current")
_FlMsModuleMvLinkRemoteDeviceType_Type = DisplayString
_FlMsModuleMvLinkRemoteDeviceType_Object = MibTableColumn
flMsModuleMvLinkRemoteDeviceType = _FlMsModuleMvLinkRemoteDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 6),
    _FlMsModuleMvLinkRemoteDeviceType_Type()
)
flMsModuleMvLinkRemoteDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRemoteDeviceType.setStatus("current")
_FlMsModuleMvLinkRemoteHwRevision_Type = DisplayString
_FlMsModuleMvLinkRemoteHwRevision_Object = MibTableColumn
flMsModuleMvLinkRemoteHwRevision = _FlMsModuleMvLinkRemoteHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 7),
    _FlMsModuleMvLinkRemoteHwRevision_Type()
)
flMsModuleMvLinkRemoteHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRemoteHwRevision.setStatus("current")
_FlMsModuleMvLinkRemoteFoDescription1_Type = DisplayString
_FlMsModuleMvLinkRemoteFoDescription1_Object = MibTableColumn
flMsModuleMvLinkRemoteFoDescription1 = _FlMsModuleMvLinkRemoteFoDescription1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 8),
    _FlMsModuleMvLinkRemoteFoDescription1_Type()
)
flMsModuleMvLinkRemoteFoDescription1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRemoteFoDescription1.setStatus("current")
_FlMsModuleMvLinkRemoteFoDescription2_Type = DisplayString
_FlMsModuleMvLinkRemoteFoDescription2_Object = MibTableColumn
flMsModuleMvLinkRemoteFoDescription2 = _FlMsModuleMvLinkRemoteFoDescription2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 1, 1, 9),
    _FlMsModuleMvLinkRemoteFoDescription2_Type()
)
flMsModuleMvLinkRemoteFoDescription2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkRemoteFoDescription2.setStatus("current")
_FlMsModuleMvLoopbackTable_Object = MibTable
flMsModuleMvLoopbackTable = _FlMsModuleMvLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2)
)
if mibBuilder.loadTexts:
    flMsModuleMvLoopbackTable.setStatus("current")
_FlMsModuleMvLoopbackEntry_Object = MibTableRow
flMsModuleMvLoopbackEntry = _FlMsModuleMvLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1)
)
flMsModuleMvLoopbackEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkIndex"),
)
if mibBuilder.loadTexts:
    flMsModuleMvLoopbackEntry.setStatus("current")


class _FlMsModuleMvLinkLoopbackTest_Type(Integer32):
    """Custom type flMsModuleMvLinkLoopbackTest based on Integer32"""
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
        *(("autoSingle", 1),
          ("autoMultiple", 2),
          ("manFrameCount", 3),
          ("manTimed", 4))
    )


_FlMsModuleMvLinkLoopbackTest_Type.__name__ = "Integer32"
_FlMsModuleMvLinkLoopbackTest_Object = MibTableColumn
flMsModuleMvLinkLoopbackTest = _FlMsModuleMvLinkLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1, 1),
    _FlMsModuleMvLinkLoopbackTest_Type()
)
flMsModuleMvLinkLoopbackTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsModuleMvLinkLoopbackTest.setStatus("current")


class _FlMsModuleMvLinkLoopbackCountVal_Type(Integer32):
    """Custom type flMsModuleMvLinkLoopbackCountVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_FlMsModuleMvLinkLoopbackCountVal_Type.__name__ = "Integer32"
_FlMsModuleMvLinkLoopbackCountVal_Object = MibTableColumn
flMsModuleMvLinkLoopbackCountVal = _FlMsModuleMvLinkLoopbackCountVal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1, 2),
    _FlMsModuleMvLinkLoopbackCountVal_Type()
)
flMsModuleMvLinkLoopbackCountVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsModuleMvLinkLoopbackCountVal.setStatus("current")


class _FlMsModuleMvLinkLoopbackTimeVal_Type(Integer32):
    """Custom type flMsModuleMvLinkLoopbackTimeVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_FlMsModuleMvLinkLoopbackTimeVal_Type.__name__ = "Integer32"
_FlMsModuleMvLinkLoopbackTimeVal_Object = MibTableColumn
flMsModuleMvLinkLoopbackTimeVal = _FlMsModuleMvLinkLoopbackTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1, 3),
    _FlMsModuleMvLinkLoopbackTimeVal_Type()
)
flMsModuleMvLinkLoopbackTimeVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsModuleMvLinkLoopbackTimeVal.setStatus("current")


class _FlMsModuleMvLinkLoopbackRun_Type(Integer32):
    """Custom type flMsModuleMvLinkLoopbackRun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stanby", 1),
          ("run", 2))
    )


_FlMsModuleMvLinkLoopbackRun_Type.__name__ = "Integer32"
_FlMsModuleMvLinkLoopbackRun_Object = MibTableColumn
flMsModuleMvLinkLoopbackRun = _FlMsModuleMvLinkLoopbackRun_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1, 4),
    _FlMsModuleMvLinkLoopbackRun_Type()
)
flMsModuleMvLinkLoopbackRun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsModuleMvLinkLoopbackRun.setStatus("current")
_FlMsModuleMvLinkLoopbackTstRsSnt_Type = Integer32
_FlMsModuleMvLinkLoopbackTstRsSnt_Object = MibTableColumn
flMsModuleMvLinkLoopbackTstRsSnt = _FlMsModuleMvLinkLoopbackTstRsSnt_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1, 5),
    _FlMsModuleMvLinkLoopbackTstRsSnt_Type()
)
flMsModuleMvLinkLoopbackTstRsSnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkLoopbackTstRsSnt.setStatus("current")
_FlMsModuleMvLinkLoopbackTstRsRcv_Type = Integer32
_FlMsModuleMvLinkLoopbackTstRsRcv_Object = MibTableColumn
flMsModuleMvLinkLoopbackTstRsRcv = _FlMsModuleMvLinkLoopbackTstRsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1, 6),
    _FlMsModuleMvLinkLoopbackTstRsRcv_Type()
)
flMsModuleMvLinkLoopbackTstRsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkLoopbackTstRsRcv.setStatus("current")
_FlMsModuleMvLinkLoopbackTstRsRat_Type = Integer32
_FlMsModuleMvLinkLoopbackTstRsRat_Object = MibTableColumn
flMsModuleMvLinkLoopbackTstRsRat = _FlMsModuleMvLinkLoopbackTstRsRat_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 20, 2, 1, 7),
    _FlMsModuleMvLinkLoopbackTstRsRat_Type()
)
flMsModuleMvLinkLoopbackTstRsRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsModuleMvLinkLoopbackTstRsRat.setStatus("current")

# Managed Objects groups

flMsModuleMvChannelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 1, 2, 1)
)
flMsModuleMvChannelsGroup.setObjects(
    ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelIndex")
)
if mibBuilder.loadTexts:
    flMsModuleMvChannelsGroup.setStatus("current")

flMsModuleMvLinksGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 1, 2, 2)
)
flMsModuleMvLinksGroup.setObjects(
      *(("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkIndex"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRemoteDevice"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRemoteState"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRestoreDefaults"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRemoteSerialNumber"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRemoteDeviceType"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRemoteHwRevision"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRemoteFoDescription1"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkRemoteFoDescription2"))
)
if mibBuilder.loadTexts:
    flMsModuleMvLinksGroup.setStatus("current")

flMsModuleMvLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 1, 2, 3)
)
flMsModuleMvLoopbackGroup.setObjects(
      *(("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkLoopbackTest"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkLoopbackCountVal"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkLoopbackTimeVal"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkLoopbackRun"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkLoopbackTstRsSnt"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkLoopbackTstRsRcv"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinkLoopbackTstRsRat"))
)
if mibBuilder.loadTexts:
    flMsModuleMvLoopbackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMsModuleMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 1, 1, 1)
)
flMsModuleMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModulesGroup"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelsGroup"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinksGroup"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLoopbackGroup"))
)
if mibBuilder.loadTexts:
    flMsModuleMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-MSMODULE",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMsModuleMIBConformance": flMsModuleMIBConformance,
       "flMsModuleMIBCompliances": flMsModuleMIBCompliances,
       "flMsModuleMIBCompliance": flMsModuleMIBCompliance,
       "flMsModuleMIBGroups": flMsModuleMIBGroups,
       "flMsModuleMvChannelsGroup": flMsModuleMvChannelsGroup,
       "flMsModuleMvLinksGroup": flMsModuleMvLinksGroup,
       "flMsModuleMvLoopbackGroup": flMsModuleMvLoopbackGroup,
       "flMsModuleChannelsMv": flMsModuleChannelsMv,
       "flMsModuleMvChannelTable": flMsModuleMvChannelTable,
       "flMsModuleMvChannelEntry": flMsModuleMvChannelEntry,
       "flMsModuleMvChannelIndex": flMsModuleMvChannelIndex,
       "flMsModuleLinksMv": flMsModuleLinksMv,
       "flMsModuleMvLinkTable": flMsModuleMvLinkTable,
       "flMsModuleMvLinkEntry": flMsModuleMvLinkEntry,
       "flMsModuleMvLinkIndex": flMsModuleMvLinkIndex,
       "flMsModuleMvLinkRemoteDevice": flMsModuleMvLinkRemoteDevice,
       "flMsModuleMvLinkRemoteState": flMsModuleMvLinkRemoteState,
       "flMsModuleMvLinkRestoreDefaults": flMsModuleMvLinkRestoreDefaults,
       "flMsModuleMvLinkRemoteSerialNumber": flMsModuleMvLinkRemoteSerialNumber,
       "flMsModuleMvLinkRemoteDeviceType": flMsModuleMvLinkRemoteDeviceType,
       "flMsModuleMvLinkRemoteHwRevision": flMsModuleMvLinkRemoteHwRevision,
       "flMsModuleMvLinkRemoteFoDescription1": flMsModuleMvLinkRemoteFoDescription1,
       "flMsModuleMvLinkRemoteFoDescription2": flMsModuleMvLinkRemoteFoDescription2,
       "flMsModuleMvLoopbackTable": flMsModuleMvLoopbackTable,
       "flMsModuleMvLoopbackEntry": flMsModuleMvLoopbackEntry,
       "flMsModuleMvLinkLoopbackTest": flMsModuleMvLinkLoopbackTest,
       "flMsModuleMvLinkLoopbackCountVal": flMsModuleMvLinkLoopbackCountVal,
       "flMsModuleMvLinkLoopbackTimeVal": flMsModuleMvLinkLoopbackTimeVal,
       "flMsModuleMvLinkLoopbackRun": flMsModuleMvLinkLoopbackRun,
       "flMsModuleMvLinkLoopbackTstRsSnt": flMsModuleMvLinkLoopbackTstRsSnt,
       "flMsModuleMvLinkLoopbackTstRsRcv": flMsModuleMvLinkLoopbackTstRsRcv,
       "flMsModuleMvLinkLoopbackTstRsRat": flMsModuleMvLinkLoopbackTstRsRat}
)
