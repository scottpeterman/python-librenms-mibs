# SNMP MIB module (ARRIS-C3-CMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\ARRIS-C3-CMM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:01 2025
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

(cmtsC3,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "cmtsC3")

(TenthdBmV,
 docsIfCmtsCmStatusDocsisRegMode,
 docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIpAddress,
 docsIfCmtsCmStatusMacAddress) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV",
    "docsIfCmtsCmStatusDocsisRegMode",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIpAddress",
    "docsIfCmtsCmStatusMacAddress")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cmtsC3CMMMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5)
)
if mibBuilder.loadTexts:
    cmtsC3CMMMIB.setRevisions(
        ("2005-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcxCMMObjects_ObjectIdentity = ObjectIdentity
dcxCMMObjects = _DcxCMMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1)
)
_DcxCMMCmtsCmStatusTable_Object = MibTable
dcxCMMCmtsCmStatusTable = _DcxCMMCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dcxCMMCmtsCmStatusTable.setStatus("current")
_DcxCMMCmtsCmStatusEntry_Object = MibTableRow
dcxCMMCmtsCmStatusEntry = _DcxCMMCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcxCMMCmtsCmStatusEntry.setStatus("current")
_DcxCMMCmDebugLevel_Type = Unsigned32
_DcxCMMCmDebugLevel_Object = MibTableColumn
dcxCMMCmDebugLevel = _DcxCMMCmDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1, 1),
    _DcxCMMCmDebugLevel_Type()
)
dcxCMMCmDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxCMMCmDebugLevel.setStatus("current")
_DcxCMMUpDisable_Type = Unsigned32
_DcxCMMUpDisable_Object = MibTableColumn
dcxCMMUpDisable = _DcxCMMUpDisable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1, 2),
    _DcxCMMUpDisable_Type()
)
dcxCMMUpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxCMMUpDisable.setStatus("current")


class _DcxCMMResetCm_Type(Integer32):
    """Custom type dcxCMMResetCm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("delete", 2),
          ("none", 3))
    )


_DcxCMMResetCm_Type.__name__ = "Integer32"
_DcxCMMResetCm_Object = MibTableColumn
dcxCMMResetCm = _DcxCMMResetCm_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1, 3),
    _DcxCMMResetCm_Type()
)
dcxCMMResetCm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxCMMResetCm.setStatus("current")
_DcxCMMResetCounters_Type = TruthValue
_DcxCMMResetCounters_Object = MibTableColumn
dcxCMMResetCounters = _DcxCMMResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1, 4),
    _DcxCMMResetCounters_Type()
)
dcxCMMResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcxCMMResetCounters.setStatus("current")


class _DcxCMMCmBpiState_Type(Integer32):
    """Custom type dcxCMMCmBpiState based on Integer32"""
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
        *(("cmBPI2NotManagedByBPI2", 0),
          ("cmBPI2InBPI2Progress", 1),
          ("cmBPI2NotAuthorized", 2),
          ("cmBPI2KeyIssued", 3),
          ("cmBPI2IsRunning", 4))
    )


_DcxCMMCmBpiState_Type.__name__ = "Integer32"
_DcxCMMCmBpiState_Object = MibTableColumn
dcxCMMCmBpiState = _DcxCMMCmBpiState_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1, 5),
    _DcxCMMCmBpiState_Type()
)
dcxCMMCmBpiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMCmBpiState.setStatus("current")
_DcxCMMCmPrimaryUsSf_Type = Unsigned32
_DcxCMMCmPrimaryUsSf_Object = MibTableColumn
dcxCMMCmPrimaryUsSf = _DcxCMMCmPrimaryUsSf_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1, 6),
    _DcxCMMCmPrimaryUsSf_Type()
)
dcxCMMCmPrimaryUsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMCmPrimaryUsSf.setStatus("current")
_DcxCMMCmPrimaryDsSf_Type = Unsigned32
_DcxCMMCmPrimaryDsSf_Object = MibTableColumn
dcxCMMCmPrimaryDsSf = _DcxCMMCmPrimaryDsSf_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 1, 1, 7),
    _DcxCMMCmPrimaryDsSf_Type()
)
dcxCMMCmPrimaryDsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMCmPrimaryDsSf.setStatus("current")
_DcxCMMIpToCmTable_Object = MibTable
dcxCMMIpToCmTable = _DcxCMMIpToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    dcxCMMIpToCmTable.setStatus("current")
_DcxCMMIpToCmEntry_Object = MibTableRow
dcxCMMIpToCmEntry = _DcxCMMIpToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 2, 1)
)
dcxCMMIpToCmEntry.setIndexNames(
    (0, "ARRIS-C3-CMM-MIB", "dcxCMMCmIp"),
)
if mibBuilder.loadTexts:
    dcxCMMIpToCmEntry.setStatus("current")
_DcxCMMCmIp_Type = IpAddress
_DcxCMMCmIp_Object = MibTableColumn
dcxCMMCmIp = _DcxCMMCmIp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 2, 1, 1),
    _DcxCMMCmIp_Type()
)
dcxCMMCmIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcxCMMCmIp.setStatus("current")


class _DcxCMMCmPtr_Type(Integer32):
    """Custom type dcxCMMCmPtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DcxCMMCmPtr_Type.__name__ = "Integer32"
_DcxCMMCmPtr_Object = MibTableColumn
dcxCMMCmPtr = _DcxCMMCmPtr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 2, 1, 2),
    _DcxCMMCmPtr_Type()
)
dcxCMMCmPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMCmPtr.setStatus("current")
_DcxCMMFlapTable_Object = MibTable
dcxCMMFlapTable = _DcxCMMFlapTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    dcxCMMFlapTable.setStatus("current")
_DcxCMMCmFlapEntry_Object = MibTableRow
dcxCMMCmFlapEntry = _DcxCMMCmFlapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1)
)
dcxCMMCmFlapEntry.setIndexNames(
    (0, "ARRIS-C3-CMM-MIB", "dcxCMMFlapMacAddr"),
)
if mibBuilder.loadTexts:
    dcxCMMCmFlapEntry.setStatus("current")
_DcxCMMFlapMacAddr_Type = MacAddress
_DcxCMMFlapMacAddr_Object = MibTableColumn
dcxCMMFlapMacAddr = _DcxCMMFlapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 2),
    _DcxCMMFlapMacAddr_Type()
)
dcxCMMFlapMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapMacAddr.setStatus("current")
_DcxCMMFlapUpstreamID_Type = Unsigned32
_DcxCMMFlapUpstreamID_Object = MibTableColumn
dcxCMMFlapUpstreamID = _DcxCMMFlapUpstreamID_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 3),
    _DcxCMMFlapUpstreamID_Type()
)
dcxCMMFlapUpstreamID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapUpstreamID.setStatus("current")
_DcxCMMFlapInsertions_Type = Unsigned32
_DcxCMMFlapInsertions_Object = MibTableColumn
dcxCMMFlapInsertions = _DcxCMMFlapInsertions_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 4),
    _DcxCMMFlapInsertions_Type()
)
dcxCMMFlapInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapInsertions.setStatus("current")
_DcxCMMFlapHits_Type = Unsigned32
_DcxCMMFlapHits_Object = MibTableColumn
dcxCMMFlapHits = _DcxCMMFlapHits_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 5),
    _DcxCMMFlapHits_Type()
)
dcxCMMFlapHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapHits.setStatus("current")
_DcxCMMFlapMisses_Type = Unsigned32
_DcxCMMFlapMisses_Object = MibTableColumn
dcxCMMFlapMisses = _DcxCMMFlapMisses_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 6),
    _DcxCMMFlapMisses_Type()
)
dcxCMMFlapMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapMisses.setStatus("current")
_DcxCMMFlapCRC_Type = Unsigned32
_DcxCMMFlapCRC_Object = MibTableColumn
dcxCMMFlapCRC = _DcxCMMFlapCRC_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 7),
    _DcxCMMFlapCRC_Type()
)
dcxCMMFlapCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapCRC.setStatus("current")
_DcxCMMFlapCount_Type = Unsigned32
_DcxCMMFlapCount_Object = MibTableColumn
dcxCMMFlapCount = _DcxCMMFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 9),
    _DcxCMMFlapCount_Type()
)
dcxCMMFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapCount.setStatus("current")
_DcxCMMFlapTimeStamp_Type = Unsigned32
_DcxCMMFlapTimeStamp_Object = MibTableColumn
dcxCMMFlapTimeStamp = _DcxCMMFlapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 3, 1, 10),
    _DcxCMMFlapTimeStamp_Type()
)
dcxCMMFlapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcxCMMFlapTimeStamp.setStatus("current")
_DcxCMMTrapGroup_ObjectIdentity = ObjectIdentity
dcxCMMTrapGroup = _DcxCMMTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 4)
)


class _DcxCMMTrapReason_Type(DisplayString):
    """Custom type dcxCMMTrapReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DcxCMMTrapReason_Type.__name__ = "DisplayString"
_DcxCMMTrapReason_Object = MibScalar
dcxCMMTrapReason = _DcxCMMTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 4, 1),
    _DcxCMMTrapReason_Type()
)
dcxCMMTrapReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dcxCMMTrapReason.setStatus("current")
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("ARRIS-C3-CMM-MIB",
     "dcxCMMCmtsCmStatusEntry")
)
dcxCMMCmtsCmStatusEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups


# Notification objects

dcxCMMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 5, 1, 4, 2)
)
dcxCMMTrap.setObjects(
    ("ARRIS-C3-CMM-MIB", "dcxCMMTrapReason")
)
if mibBuilder.loadTexts:
    dcxCMMTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-C3-CMM-MIB",
    **{"cmtsC3CMMMIB": cmtsC3CMMMIB,
       "dcxCMMObjects": dcxCMMObjects,
       "dcxCMMCmtsCmStatusTable": dcxCMMCmtsCmStatusTable,
       "dcxCMMCmtsCmStatusEntry": dcxCMMCmtsCmStatusEntry,
       "dcxCMMCmDebugLevel": dcxCMMCmDebugLevel,
       "dcxCMMUpDisable": dcxCMMUpDisable,
       "dcxCMMResetCm": dcxCMMResetCm,
       "dcxCMMResetCounters": dcxCMMResetCounters,
       "dcxCMMCmBpiState": dcxCMMCmBpiState,
       "dcxCMMCmPrimaryUsSf": dcxCMMCmPrimaryUsSf,
       "dcxCMMCmPrimaryDsSf": dcxCMMCmPrimaryDsSf,
       "dcxCMMIpToCmTable": dcxCMMIpToCmTable,
       "dcxCMMIpToCmEntry": dcxCMMIpToCmEntry,
       "dcxCMMCmIp": dcxCMMCmIp,
       "dcxCMMCmPtr": dcxCMMCmPtr,
       "dcxCMMFlapTable": dcxCMMFlapTable,
       "dcxCMMCmFlapEntry": dcxCMMCmFlapEntry,
       "dcxCMMFlapMacAddr": dcxCMMFlapMacAddr,
       "dcxCMMFlapUpstreamID": dcxCMMFlapUpstreamID,
       "dcxCMMFlapInsertions": dcxCMMFlapInsertions,
       "dcxCMMFlapHits": dcxCMMFlapHits,
       "dcxCMMFlapMisses": dcxCMMFlapMisses,
       "dcxCMMFlapCRC": dcxCMMFlapCRC,
       "dcxCMMFlapCount": dcxCMMFlapCount,
       "dcxCMMFlapTimeStamp": dcxCMMFlapTimeStamp,
       "dcxCMMTrapGroup": dcxCMMTrapGroup,
       "dcxCMMTrapReason": dcxCMMTrapReason,
       "dcxCMMTrap": dcxCMMTrap}
)
