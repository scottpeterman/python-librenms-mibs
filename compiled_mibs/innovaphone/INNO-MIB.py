# SNMP MIB module (INNO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\innovaphone\INNO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:01:50 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 NotificationType,
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
    "NotificationType",
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Innovaphone_ObjectIdentity = ObjectIdentity
innovaphone = _Innovaphone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6666)
)
_Isdn_ObjectIdentity = ObjectIdentity
isdn = _Isdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6666, 1)
)
_L2Table_Object = MibTable
l2Table = _L2Table_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 1)
)
if mibBuilder.loadTexts:
    l2Table.setStatus("mandatory")
_L2Entry_Object = MibTableRow
l2Entry = _L2Entry_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 1, 1)
)
l2Entry.setIndexNames(
    (0, "INNO-MIB", "l2Label"),
)
if mibBuilder.loadTexts:
    l2Entry.setStatus("mandatory")


class _L2Label_Type(DisplayString):
    """Custom type l2Label based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_L2Label_Type.__name__ = "DisplayString"
_L2Label_Object = MibTableColumn
l2Label = _L2Label_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 1),
    _L2Label_Type()
)
l2Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2Label.setStatus("mandatory")


class _L2State_Type(Integer32):
    """Custom type l2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_L2State_Type.__name__ = "Integer32"
_L2State_Object = MibTableColumn
l2State = _L2State_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 2),
    _L2State_Type()
)
l2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2State.setStatus("mandatory")


class _L2Mode_Type(Integer32):
    """Custom type l2Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("te", 1),
          ("nt", 2))
    )


_L2Mode_Type.__name__ = "Integer32"
_L2Mode_Object = MibTableColumn
l2Mode = _L2Mode_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 3),
    _L2Mode_Type()
)
l2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l2Mode.setStatus("mandatory")


class _L1Label_Type(DisplayString):
    """Custom type l1Label based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_L1Label_Type.__name__ = "DisplayString"
_L1Label_Object = MibTableColumn
l1Label = _L1Label_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 1, 1, 4),
    _L1Label_Type()
)
l1Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1Label.setStatus("mandatory")
_L1PriTable_Object = MibTable
l1PriTable = _L1PriTable_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2)
)
if mibBuilder.loadTexts:
    l1PriTable.setStatus("mandatory")
_L1PriEntry_Object = MibTableRow
l1PriEntry = _L1PriEntry_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1)
)
l1PriEntry.setIndexNames(
    (0, "INNO-MIB", "l1PriLabel"),
)
if mibBuilder.loadTexts:
    l1PriEntry.setStatus("mandatory")


class _L1PriLabel_Type(DisplayString):
    """Custom type l1PriLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_L1PriLabel_Type.__name__ = "DisplayString"
_L1PriLabel_Object = MibTableColumn
l1PriLabel = _L1PriLabel_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 1),
    _L1PriLabel_Type()
)
l1PriLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriLabel.setStatus("mandatory")


class _L1PriState_Type(Integer32):
    """Custom type l1PriState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_L1PriState_Type.__name__ = "Integer32"
_L1PriState_Object = MibTableColumn
l1PriState = _L1PriState_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 2),
    _L1PriState_Type()
)
l1PriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriState.setStatus("mandatory")
_L1PriErrCrc4_Type = Counter32
_L1PriErrCrc4_Object = MibTableColumn
l1PriErrCrc4 = _L1PriErrCrc4_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 3),
    _L1PriErrCrc4_Type()
)
l1PriErrCrc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriErrCrc4.setStatus("mandatory")
_L1PriErrRemAlarmInd_Type = Counter32
_L1PriErrRemAlarmInd_Object = MibTableColumn
l1PriErrRemAlarmInd = _L1PriErrRemAlarmInd_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 4),
    _L1PriErrRemAlarmInd_Type()
)
l1PriErrRemAlarmInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriErrRemAlarmInd.setStatus("mandatory")
_L1PriErrSigLoss_Type = Counter32
_L1PriErrSigLoss_Object = MibTableColumn
l1PriErrSigLoss = _L1PriErrSigLoss_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 5),
    _L1PriErrSigLoss_Type()
)
l1PriErrSigLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriErrSigLoss.setStatus("mandatory")
_L1PriErrAlarmInd_Type = Counter32
_L1PriErrAlarmInd_Object = MibTableColumn
l1PriErrAlarmInd = _L1PriErrAlarmInd_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 6),
    _L1PriErrAlarmInd_Type()
)
l1PriErrAlarmInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriErrAlarmInd.setStatus("mandatory")
_L1PriErrFrameAlignmentTOut_Type = Counter32
_L1PriErrFrameAlignmentTOut_Object = MibTableColumn
l1PriErrFrameAlignmentTOut = _L1PriErrFrameAlignmentTOut_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 7),
    _L1PriErrFrameAlignmentTOut_Type()
)
l1PriErrFrameAlignmentTOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriErrFrameAlignmentTOut.setStatus("mandatory")
_L1PriErrFrameAlignmentLoss_Type = Counter32
_L1PriErrFrameAlignmentLoss_Object = MibTableColumn
l1PriErrFrameAlignmentLoss = _L1PriErrFrameAlignmentLoss_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 8),
    _L1PriErrFrameAlignmentLoss_Type()
)
l1PriErrFrameAlignmentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriErrFrameAlignmentLoss.setStatus("mandatory")
_L1PriErrSlip_Type = Counter32
_L1PriErrSlip_Object = MibTableColumn
l1PriErrSlip = _L1PriErrSlip_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 9),
    _L1PriErrSlip_Type()
)
l1PriErrSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1PriErrSlip.setStatus("mandatory")


class _L1PriTest_Type(Integer32):
    """Custom type l1PriTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTest", 0),
          ("simAlarm", 1),
          ("resetAlarms", 2))
    )


_L1PriTest_Type.__name__ = "Integer32"
_L1PriTest_Object = MibTableColumn
l1PriTest = _L1PriTest_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 2, 1, 10),
    _L1PriTest_Type()
)
l1PriTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    l1PriTest.setStatus("mandatory")
_L1BriTable_Object = MibTable
l1BriTable = _L1BriTable_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 3)
)
if mibBuilder.loadTexts:
    l1BriTable.setStatus("mandatory")
_L1BriEntry_Object = MibTableRow
l1BriEntry = _L1BriEntry_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 3, 1)
)
l1BriEntry.setIndexNames(
    (0, "INNO-MIB", "l1BriLabel"),
)
if mibBuilder.loadTexts:
    l1BriEntry.setStatus("mandatory")


class _L1BriLabel_Type(DisplayString):
    """Custom type l1BriLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_L1BriLabel_Type.__name__ = "DisplayString"
_L1BriLabel_Object = MibTableColumn
l1BriLabel = _L1BriLabel_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 3, 1, 1),
    _L1BriLabel_Type()
)
l1BriLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1BriLabel.setStatus("mandatory")


class _L1BriState_Type(Integer32):
    """Custom type l1BriState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_L1BriState_Type.__name__ = "Integer32"
_L1BriState_Object = MibTableColumn
l1BriState = _L1BriState_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 3, 1, 2),
    _L1BriState_Type()
)
l1BriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l1BriState.setStatus("mandatory")
_L3Table_Object = MibTable
l3Table = _L3Table_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 4)
)
if mibBuilder.loadTexts:
    l3Table.setStatus("mandatory")
_L3Entry_Object = MibTableRow
l3Entry = _L3Entry_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 4, 1)
)
l3Entry.setIndexNames(
    (0, "INNO-MIB", "l3Label"),
)
if mibBuilder.loadTexts:
    l3Entry.setStatus("mandatory")


class _L3Label_Type(DisplayString):
    """Custom type l3Label based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_L3Label_Type.__name__ = "DisplayString"
_L3Label_Object = MibTableColumn
l3Label = _L3Label_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 1),
    _L3Label_Type()
)
l3Label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3Label.setStatus("mandatory")


class _L3Protocol_Type(Integer32):
    """Custom type l3Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              23)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("other", 1),
          ("etsi", 3),
          ("qsig", 23))
    )


_L3Protocol_Type.__name__ = "Integer32"
_L3Protocol_Object = MibTableColumn
l3Protocol = _L3Protocol_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 2),
    _L3Protocol_Type()
)
l3Protocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3Protocol.setStatus("mandatory")
_L3NumBchan_Type = Integer32
_L3NumBchan_Object = MibTableColumn
l3NumBchan = _L3NumBchan_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 3),
    _L3NumBchan_Type()
)
l3NumBchan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3NumBchan.setStatus("mandatory")
_L3NumBchanActive_Type = Gauge32
_L3NumBchanActive_Object = MibTableColumn
l3NumBchanActive = _L3NumBchanActive_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 4),
    _L3NumBchanActive_Type()
)
l3NumBchanActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3NumBchanActive.setStatus("mandatory")
_L3CallsBoot_Type = Counter32
_L3CallsBoot_Object = MibTableColumn
l3CallsBoot = _L3CallsBoot_Object(
    (1, 3, 6, 1, 4, 1, 6666, 1, 4, 1, 5),
    _L3CallsBoot_Type()
)
l3CallsBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3CallsBoot.setStatus("mandatory")
_Gateway_ObjectIdentity = ObjectIdentity
gateway = _Gateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6666, 2)
)
_Gatekeeper_ObjectIdentity = ObjectIdentity
gatekeeper = _Gatekeeper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1)
)
_VoiceIfTable_Object = MibTable
voiceIfTable = _VoiceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1)
)
if mibBuilder.loadTexts:
    voiceIfTable.setStatus("mandatory")
_VoiceIfEntry_Object = MibTableRow
voiceIfEntry = _VoiceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1)
)
voiceIfEntry.setIndexNames(
    (0, "INNO-MIB", "voiceIfIndex"),
    (0, "INNO-MIB", "voiceIfAliasIndex"),
)
if mibBuilder.loadTexts:
    voiceIfEntry.setStatus("mandatory")


class _VoiceIfGwName_Type(DisplayString):
    """Custom type voiceIfGwName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceIfGwName_Type.__name__ = "DisplayString"
_VoiceIfGwName_Object = MibTableColumn
voiceIfGwName = _VoiceIfGwName_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 1),
    _VoiceIfGwName_Type()
)
voiceIfGwName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfGwName.setStatus("mandatory")


class _VoiceIfType_Type(Integer32):
    """Custom type voiceIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unkown", 0),
          ("if", 1),
          ("ep", 2),
          ("gk", 3),
          ("gw", 4))
    )


_VoiceIfType_Type.__name__ = "Integer32"
_VoiceIfType_Object = MibTableColumn
voiceIfType = _VoiceIfType_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 2),
    _VoiceIfType_Type()
)
voiceIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfType.setStatus("mandatory")
_VoiceIfAddr_Type = IpAddress
_VoiceIfAddr_Object = MibTableColumn
voiceIfAddr = _VoiceIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 3),
    _VoiceIfAddr_Type()
)
voiceIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfAddr.setStatus("mandatory")


class _VoiceIfState_Type(Integer32):
    """Custom type voiceIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_VoiceIfState_Type.__name__ = "Integer32"
_VoiceIfState_Object = MibTableColumn
voiceIfState = _VoiceIfState_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 4),
    _VoiceIfState_Type()
)
voiceIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfState.setStatus("mandatory")


class _VoiceIfNumber_Type(DisplayString):
    """Custom type voiceIfNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceIfNumber_Type.__name__ = "DisplayString"
_VoiceIfNumber_Object = MibTableColumn
voiceIfNumber = _VoiceIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 5),
    _VoiceIfNumber_Type()
)
voiceIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfNumber.setStatus("mandatory")


class _VoiceIfName_Type(DisplayString):
    """Custom type voiceIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceIfName_Type.__name__ = "DisplayString"
_VoiceIfName_Object = MibTableColumn
voiceIfName = _VoiceIfName_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 6),
    _VoiceIfName_Type()
)
voiceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfName.setStatus("mandatory")


class _VoiceIfProduct_Type(DisplayString):
    """Custom type voiceIfProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoiceIfProduct_Type.__name__ = "DisplayString"
_VoiceIfProduct_Object = MibTableColumn
voiceIfProduct = _VoiceIfProduct_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 7),
    _VoiceIfProduct_Type()
)
voiceIfProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfProduct.setStatus("mandatory")


class _VoiceIfIndex_Type(Integer32):
    """Custom type voiceIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VoiceIfIndex_Type.__name__ = "Integer32"
_VoiceIfIndex_Object = MibTableColumn
voiceIfIndex = _VoiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 8),
    _VoiceIfIndex_Type()
)
voiceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfIndex.setStatus("mandatory")


class _VoiceIfAliasIndex_Type(Integer32):
    """Custom type voiceIfAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VoiceIfAliasIndex_Type.__name__ = "Integer32"
_VoiceIfAliasIndex_Object = MibTableColumn
voiceIfAliasIndex = _VoiceIfAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 6666, 2, 1, 1, 1, 9),
    _VoiceIfAliasIndex_Type()
)
voiceIfAliasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceIfAliasIndex.setStatus("optional")
_TrapDummyGroup_ObjectIdentity = ObjectIdentity
trapDummyGroup = _TrapDummyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6666, 3)
)


class _TrapDisplayStringParm_Type(DisplayString):
    """Custom type trapDisplayStringParm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrapDisplayStringParm_Type.__name__ = "DisplayString"
_TrapDisplayStringParm_Object = MibScalar
trapDisplayStringParm = _TrapDisplayStringParm_Object(
    (1, 3, 6, 1, 4, 1, 6666, 3, 1),
    _TrapDisplayStringParm_Type()
)
trapDisplayStringParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDisplayStringParm.setStatus("mandatory")


class _TrapIntegerParm_Type(Integer32):
    """Custom type trapIntegerParm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapIntegerParm_Type.__name__ = "Integer32"
_TrapIntegerParm_Object = MibScalar
trapIntegerParm = _TrapIntegerParm_Object(
    (1, 3, 6, 1, 4, 1, 6666, 3, 2),
    _TrapIntegerParm_Type()
)
trapIntegerParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIntegerParm.setStatus("mandatory")
_TrapGaugeParm_Type = Gauge32
_TrapGaugeParm_Object = MibScalar
trapGaugeParm = _TrapGaugeParm_Object(
    (1, 3, 6, 1, 4, 1, 6666, 3, 3),
    _TrapGaugeParm_Type()
)
trapGaugeParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapGaugeParm.setStatus("mandatory")

# Managed Objects groups


# Notification objects

innoColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 0)
)
if mibBuilder.loadTexts:
    innoColdStart.setStatus(
        ""
    )

innoWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 1)
)
if mibBuilder.loadTexts:
    innoWarmStart.setStatus(
        ""
    )

innoLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 2)
)
innoLinkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    innoLinkDown.setStatus(
        ""
    )

innoLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 3)
)
innoLinkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    innoLinkUp.setStatus(
        ""
    )

innoAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 4)
)
if mibBuilder.loadTexts:
    innoAuthenticationFailure.setStatus(
        ""
    )

innoIsdnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 5)
)
innoIsdnFailure.setObjects(
      *(("INNO-MIB", "trapDisplayStringParm"),
        ("INNO-MIB", "trapIntegerParm"))
)
if mibBuilder.loadTexts:
    innoIsdnFailure.setStatus(
        ""
    )

innoDiagAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 6)
)
innoDiagAlarm.setObjects(
      *(("INNO-MIB", "trapGaugeParm"),
        ("INNO-MIB", "trapDisplayStringParm"),
        ("INNO-MIB", "trapGaugeParm"),
        ("INNO-MIB", "trapDisplayStringParm"))
)
if mibBuilder.loadTexts:
    innoDiagAlarm.setStatus(
        ""
    )

innoDiagAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6666, 0, 7)
)
innoDiagAlarmClear.setObjects(
      *(("INNO-MIB", "trapGaugeParm"),
        ("INNO-MIB", "trapDisplayStringParm"))
)
if mibBuilder.loadTexts:
    innoDiagAlarmClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INNO-MIB",
    **{"DisplayString": DisplayString,
       "innovaphone": innovaphone,
       "innoColdStart": innoColdStart,
       "innoWarmStart": innoWarmStart,
       "innoLinkDown": innoLinkDown,
       "innoLinkUp": innoLinkUp,
       "innoAuthenticationFailure": innoAuthenticationFailure,
       "innoIsdnFailure": innoIsdnFailure,
       "innoDiagAlarm": innoDiagAlarm,
       "innoDiagAlarmClear": innoDiagAlarmClear,
       "isdn": isdn,
       "l2Table": l2Table,
       "l2Entry": l2Entry,
       "l2Label": l2Label,
       "l2State": l2State,
       "l2Mode": l2Mode,
       "l1Label": l1Label,
       "l1PriTable": l1PriTable,
       "l1PriEntry": l1PriEntry,
       "l1PriLabel": l1PriLabel,
       "l1PriState": l1PriState,
       "l1PriErrCrc4": l1PriErrCrc4,
       "l1PriErrRemAlarmInd": l1PriErrRemAlarmInd,
       "l1PriErrSigLoss": l1PriErrSigLoss,
       "l1PriErrAlarmInd": l1PriErrAlarmInd,
       "l1PriErrFrameAlignmentTOut": l1PriErrFrameAlignmentTOut,
       "l1PriErrFrameAlignmentLoss": l1PriErrFrameAlignmentLoss,
       "l1PriErrSlip": l1PriErrSlip,
       "l1PriTest": l1PriTest,
       "l1BriTable": l1BriTable,
       "l1BriEntry": l1BriEntry,
       "l1BriLabel": l1BriLabel,
       "l1BriState": l1BriState,
       "l3Table": l3Table,
       "l3Entry": l3Entry,
       "l3Label": l3Label,
       "l3Protocol": l3Protocol,
       "l3NumBchan": l3NumBchan,
       "l3NumBchanActive": l3NumBchanActive,
       "l3CallsBoot": l3CallsBoot,
       "gateway": gateway,
       "gatekeeper": gatekeeper,
       "voiceIfTable": voiceIfTable,
       "voiceIfEntry": voiceIfEntry,
       "voiceIfGwName": voiceIfGwName,
       "voiceIfType": voiceIfType,
       "voiceIfAddr": voiceIfAddr,
       "voiceIfState": voiceIfState,
       "voiceIfNumber": voiceIfNumber,
       "voiceIfName": voiceIfName,
       "voiceIfProduct": voiceIfProduct,
       "voiceIfIndex": voiceIfIndex,
       "voiceIfAliasIndex": voiceIfAliasIndex,
       "trapDummyGroup": trapDummyGroup,
       "trapDisplayStringParm": trapDisplayStringParm,
       "trapIntegerParm": trapIntegerParm,
       "trapGaugeParm": trapGaugeParm}
)
