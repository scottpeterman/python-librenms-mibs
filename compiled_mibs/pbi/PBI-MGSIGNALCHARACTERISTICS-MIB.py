# SNMP MIB module (PBI-MGSIGNALCHARACTERISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pbi\PBI-MGSIGNALCHARACTERISTICS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:29 2025
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

(mg,) = mibBuilder.importSymbols(
    "PBI-MAIN-MIB",
    "mg")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mgSignalCharacteristics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2)
)
if mibBuilder.loadTexts:
    mgSignalCharacteristics.setRevisions(
        ("2006-09-21 09:24",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TsOutTable_Object = MibTable
tsOutTable = _TsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tsOutTable.setStatus("current")
_TsOutEntry_Object = MibTableRow
tsOutEntry = _TsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1)
)
tsOutEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelOutput"),
)
if mibBuilder.loadTexts:
    tsOutEntry.setStatus("current")
_ChannelOutput_Type = Integer32
_ChannelOutput_Object = MibTableColumn
channelOutput = _ChannelOutput_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 1),
    _ChannelOutput_Type()
)
channelOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelOutput.setStatus("current")
_BitRate_Type = Integer32
_BitRate_Object = MibTableColumn
bitRate = _BitRate_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 2),
    _BitRate_Type()
)
bitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bitRate.setStatus("current")
_PacketSize_Type = Integer32
_PacketSize_Object = MibTableColumn
packetSize = _PacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 3),
    _PacketSize_Type()
)
packetSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    packetSize.setStatus("current")
_TransportStreamID_Type = Integer32
_TransportStreamID_Object = MibTableColumn
transportStreamID = _TransportStreamID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 4),
    _TransportStreamID_Type()
)
transportStreamID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportStreamID.setStatus("current")
_OtiginalNetworkID_Type = Integer32
_OtiginalNetworkID_Object = MibTableColumn
otiginalNetworkID = _OtiginalNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 5),
    _OtiginalNetworkID_Type()
)
otiginalNetworkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otiginalNetworkID.setStatus("current")
_NetworkID_Type = Integer32
_NetworkID_Object = MibTableColumn
networkID = _NetworkID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 6),
    _NetworkID_Type()
)
networkID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkID.setStatus("current")
_BitrateThreshosdPercent_Type = Integer32
_BitrateThreshosdPercent_Object = MibTableColumn
bitrateThreshosdPercent = _BitrateThreshosdPercent_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 7),
    _BitrateThreshosdPercent_Type()
)
bitrateThreshosdPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bitrateThreshosdPercent.setStatus("current")
_OutValidBitRate_Type = Integer32
_OutValidBitRate_Object = MibTableColumn
outValidBitRate = _OutValidBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 1, 1, 8),
    _OutValidBitRate_Type()
)
outValidBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outValidBitRate.setStatus("current")
_MgPATTable_Object = MibTable
mgPATTable = _MgPATTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mgPATTable.setStatus("current")
_MgPATEntry_Object = MibTableRow
mgPATEntry = _MgPATEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 2, 1)
)
mgPATEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelInputPAT"),
)
if mibBuilder.loadTexts:
    mgPATEntry.setStatus("current")


class _ChannelInputPAT_Type(Integer32):
    """Custom type channelInputPAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ChannelInputPAT_Type.__name__ = "Integer32"
_ChannelInputPAT_Object = MibTableColumn
channelInputPAT = _ChannelInputPAT_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 2, 1, 1),
    _ChannelInputPAT_Type()
)
channelInputPAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInputPAT.setStatus("current")


class _PatSection_Type(DisplayString):
    """Custom type patSection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PatSection_Type.__name__ = "DisplayString"
_PatSection_Object = MibTableColumn
patSection = _PatSection_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 2, 1, 2),
    _PatSection_Type()
)
patSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    patSection.setStatus("current")
_MgPMTTable_Object = MibTable
mgPMTTable = _MgPMTTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 3)
)
if mibBuilder.loadTexts:
    mgPMTTable.setStatus("current")
_MgPMTEntry_Object = MibTableRow
mgPMTEntry = _MgPMTEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 3, 1)
)
mgPMTEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelInputPMT"),
)
if mibBuilder.loadTexts:
    mgPMTEntry.setStatus("current")
_ChannelInputPMT_Type = Integer32
_ChannelInputPMT_Object = MibTableColumn
channelInputPMT = _ChannelInputPMT_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 3, 1, 1),
    _ChannelInputPMT_Type()
)
channelInputPMT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInputPMT.setStatus("current")
_PmtProgramNumber_Type = Integer32
_PmtProgramNumber_Object = MibTableColumn
pmtProgramNumber = _PmtProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 3, 1, 2),
    _PmtProgramNumber_Type()
)
pmtProgramNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmtProgramNumber.setStatus("current")
_PmtPID_Type = Integer32
_PmtPID_Object = MibTableColumn
pmtPID = _PmtPID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 3, 1, 3),
    _PmtPID_Type()
)
pmtPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmtPID.setStatus("current")


class _PmtSection_Type(DisplayString):
    """Custom type pmtSection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PmtSection_Type.__name__ = "DisplayString"
_PmtSection_Object = MibTableColumn
pmtSection = _PmtSection_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 3, 1, 4),
    _PmtSection_Type()
)
pmtSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmtSection.setStatus("current")
_MgNITTable_Object = MibTable
mgNITTable = _MgNITTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 4)
)
if mibBuilder.loadTexts:
    mgNITTable.setStatus("current")
_MgNITEntry_Object = MibTableRow
mgNITEntry = _MgNITEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 4, 1)
)
mgNITEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelInputNIT"),
)
if mibBuilder.loadTexts:
    mgNITEntry.setStatus("current")
_ChannelInputNIT_Type = Integer32
_ChannelInputNIT_Object = MibTableColumn
channelInputNIT = _ChannelInputNIT_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 4, 1, 1),
    _ChannelInputNIT_Type()
)
channelInputNIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInputNIT.setStatus("current")
_NetworkType_Type = Integer32
_NetworkType_Object = MibTableColumn
networkType = _NetworkType_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 4, 1, 2),
    _NetworkType_Type()
)
networkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkType.setStatus("current")


class _NitActualSection_Type(DisplayString):
    """Custom type nitActualSection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_NitActualSection_Type.__name__ = "DisplayString"
_NitActualSection_Object = MibTableColumn
nitActualSection = _NitActualSection_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 4, 1, 3),
    _NitActualSection_Type()
)
nitActualSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nitActualSection.setStatus("current")


class _NitOhtersSection_Type(DisplayString):
    """Custom type nitOhtersSection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_NitOhtersSection_Type.__name__ = "DisplayString"
_NitOhtersSection_Object = MibTableColumn
nitOhtersSection = _NitOhtersSection_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 4, 1, 4),
    _NitOhtersSection_Type()
)
nitOhtersSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nitOhtersSection.setStatus("current")
_MgSDTTable_Object = MibTable
mgSDTTable = _MgSDTTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 5)
)
if mibBuilder.loadTexts:
    mgSDTTable.setStatus("current")
_MgSDTEntry_Object = MibTableRow
mgSDTEntry = _MgSDTEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 5, 1)
)
mgSDTEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelInputSDT"),
)
if mibBuilder.loadTexts:
    mgSDTEntry.setStatus("current")
_ChannelInputSDT_Type = Integer32
_ChannelInputSDT_Object = MibTableColumn
channelInputSDT = _ChannelInputSDT_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 5, 1, 1),
    _ChannelInputSDT_Type()
)
channelInputSDT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInputSDT.setStatus("current")


class _SdtSection_Type(DisplayString):
    """Custom type sdtSection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SdtSection_Type.__name__ = "DisplayString"
_SdtSection_Object = MibTableColumn
sdtSection = _SdtSection_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 5, 1, 2),
    _SdtSection_Type()
)
sdtSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdtSection.setStatus("current")
_MgFilterTable_Object = MibTable
mgFilterTable = _MgFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 6)
)
if mibBuilder.loadTexts:
    mgFilterTable.setStatus("current")
_MgFilterEntry_Object = MibTableRow
mgFilterEntry = _MgFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 6, 1)
)
mgFilterEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelInputFilter"),
)
if mibBuilder.loadTexts:
    mgFilterEntry.setStatus("current")
_ChannelInputFilter_Type = Integer32
_ChannelInputFilter_Object = MibTableColumn
channelInputFilter = _ChannelInputFilter_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 6, 1, 1),
    _ChannelInputFilter_Type()
)
channelInputFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInputFilter.setStatus("current")


class _OldPID_Type(DisplayString):
    """Custom type oldPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OldPID_Type.__name__ = "DisplayString"
_OldPID_Object = MibTableColumn
oldPID = _OldPID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 6, 1, 2),
    _OldPID_Type()
)
oldPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldPID.setStatus("current")


class _NewPID_Type(DisplayString):
    """Custom type newPID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_NewPID_Type.__name__ = "DisplayString"
_NewPID_Object = MibTableColumn
newPID = _NewPID_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 6, 1, 3),
    _NewPID_Type()
)
newPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newPID.setStatus("current")


class _OldProgramNumber_Type(DisplayString):
    """Custom type oldProgramNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_OldProgramNumber_Type.__name__ = "DisplayString"
_OldProgramNumber_Object = MibTableColumn
oldProgramNumber = _OldProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 6, 1, 4),
    _OldProgramNumber_Type()
)
oldProgramNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldProgramNumber.setStatus("current")


class _NewProgramNumber_Type(DisplayString):
    """Custom type newProgramNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_NewProgramNumber_Type.__name__ = "DisplayString"
_NewProgramNumber_Object = MibTableColumn
newProgramNumber = _NewProgramNumber_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 6, 1, 5),
    _NewProgramNumber_Type()
)
newProgramNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    newProgramNumber.setStatus("current")
_MgCATTable_Object = MibTable
mgCATTable = _MgCATTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 7)
)
if mibBuilder.loadTexts:
    mgCATTable.setStatus("current")
_MgCATEntry_Object = MibTableRow
mgCATEntry = _MgCATEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 7, 1)
)
mgCATEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelInputCAT"),
)
if mibBuilder.loadTexts:
    mgCATEntry.setStatus("current")


class _ChannelInputCAT_Type(Integer32):
    """Custom type channelInputCAT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_ChannelInputCAT_Type.__name__ = "Integer32"
_ChannelInputCAT_Object = MibTableColumn
channelInputCAT = _ChannelInputCAT_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 7, 1, 1),
    _ChannelInputCAT_Type()
)
channelInputCAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInputCAT.setStatus("current")


class _CatSection_Type(DisplayString):
    """Custom type catSection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CatSection_Type.__name__ = "DisplayString"
_CatSection_Object = MibTableColumn
catSection = _CatSection_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 7, 1, 2),
    _CatSection_Type()
)
catSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    catSection.setStatus("current")
_TsInput_ObjectIdentity = ObjectIdentity
tsInput = _TsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 8)
)
_ChannelInput_Type = Integer32
_ChannelInput_Object = MibScalar
channelInput = _ChannelInput_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 8, 1),
    _ChannelInput_Type()
)
channelInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelInput.setStatus("current")
_StateLock_Type = Integer32
_StateLock_Object = MibScalar
stateLock = _StateLock_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 8, 2),
    _StateLock_Type()
)
stateLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stateLock.setStatus("current")
_TsIdPreference_Type = Integer32
_TsIdPreference_Object = MibScalar
tsIdPreference = _TsIdPreference_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 8, 3),
    _TsIdPreference_Type()
)
tsIdPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsIdPreference.setStatus("current")
_MgBATTable_Object = MibTable
mgBATTable = _MgBATTable_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 9)
)
if mibBuilder.loadTexts:
    mgBATTable.setStatus("current")
_MgBATEntry_Object = MibTableRow
mgBATEntry = _MgBATEntry_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 9, 1)
)
mgBATEntry.setIndexNames(
    (0, "PBI-MGSIGNALCHARACTERISTICS-MIB", "channelBAT"),
)
if mibBuilder.loadTexts:
    mgBATEntry.setStatus("current")
_ChannelBAT_Type = Integer32
_ChannelBAT_Object = MibTableColumn
channelBAT = _ChannelBAT_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 9, 1, 1),
    _ChannelBAT_Type()
)
channelBAT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelBAT.setStatus("current")


class _BatSection_Type(DisplayString):
    """Custom type batSection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_BatSection_Type.__name__ = "DisplayString"
_BatSection_Object = MibTableColumn
batSection = _BatSection_Object(
    (1, 3, 6, 1, 4, 1, 1070, 3, 2, 9, 1, 2),
    _BatSection_Type()
)
batSection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    batSection.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PBI-MGSIGNALCHARACTERISTICS-MIB",
    **{"mgSignalCharacteristics": mgSignalCharacteristics,
       "tsOutTable": tsOutTable,
       "tsOutEntry": tsOutEntry,
       "channelOutput": channelOutput,
       "bitRate": bitRate,
       "packetSize": packetSize,
       "transportStreamID": transportStreamID,
       "otiginalNetworkID": otiginalNetworkID,
       "networkID": networkID,
       "bitrateThreshosdPercent": bitrateThreshosdPercent,
       "outValidBitRate": outValidBitRate,
       "mgPATTable": mgPATTable,
       "mgPATEntry": mgPATEntry,
       "channelInputPAT": channelInputPAT,
       "patSection": patSection,
       "mgPMTTable": mgPMTTable,
       "mgPMTEntry": mgPMTEntry,
       "channelInputPMT": channelInputPMT,
       "pmtProgramNumber": pmtProgramNumber,
       "pmtPID": pmtPID,
       "pmtSection": pmtSection,
       "mgNITTable": mgNITTable,
       "mgNITEntry": mgNITEntry,
       "channelInputNIT": channelInputNIT,
       "networkType": networkType,
       "nitActualSection": nitActualSection,
       "nitOhtersSection": nitOhtersSection,
       "mgSDTTable": mgSDTTable,
       "mgSDTEntry": mgSDTEntry,
       "channelInputSDT": channelInputSDT,
       "sdtSection": sdtSection,
       "mgFilterTable": mgFilterTable,
       "mgFilterEntry": mgFilterEntry,
       "channelInputFilter": channelInputFilter,
       "oldPID": oldPID,
       "newPID": newPID,
       "oldProgramNumber": oldProgramNumber,
       "newProgramNumber": newProgramNumber,
       "mgCATTable": mgCATTable,
       "mgCATEntry": mgCATEntry,
       "channelInputCAT": channelInputCAT,
       "catSection": catSection,
       "tsInput": tsInput,
       "channelInput": channelInput,
       "stateLock": stateLock,
       "tsIdPreference": tsIdPreference,
       "mgBATTable": mgBATTable,
       "mgBATEntry": mgBATEntry,
       "channelBAT": channelBAT,
       "batSection": batSection}
)
