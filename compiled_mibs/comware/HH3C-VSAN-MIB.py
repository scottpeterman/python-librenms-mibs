# SNMP MIB module (HH3C-VSAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\comware\HH3C-VSAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:31:29 2025
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

(Hh3cFcAddressId,
 Hh3cFcDmState,
 Hh3cFcDomainId,
 Hh3cFcDomainIdList,
 Hh3cFcDomainIdOrZero,
 Hh3cFcDomainPriority,
 Hh3cFcNameId,
 Hh3cFcNameIdOrZero,
 Hh3cFcVsanIndex) = mibBuilder.importSymbols(
    "HH3C-FC-TC-MIB",
    "Hh3cFcAddressId",
    "Hh3cFcDmState",
    "Hh3cFcDomainId",
    "Hh3cFcDomainIdList",
    "Hh3cFcDomainIdOrZero",
    "Hh3cFcDomainPriority",
    "Hh3cFcNameId",
    "Hh3cFcNameIdOrZero",
    "Hh3cFcVsanIndex")

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hh3cSan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127)
)
if mibBuilder.loadTexts:
    hh3cSan.setRevisions(
        ("2014-07-25 18:40",
         "2014-05-09 18:40",
         "2014-03-04 15:50",
         "2013-02-28 09:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVsan_ObjectIdentity = ObjectIdentity
hh3cVsan = _Hh3cVsan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1)
)
_Hh3cVsanMibObjects_ObjectIdentity = ObjectIdentity
hh3cVsanMibObjects = _Hh3cVsanMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1)
)
_Hh3cVsanDmConfiguration_ObjectIdentity = ObjectIdentity
hh3cVsanDmConfiguration = _Hh3cVsanDmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1)
)
_Hh3cVsanTable_Object = MibTable
hh3cVsanTable = _Hh3cVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVsanTable.setStatus("current")
_Hh3cVsanEntry_Object = MibTableRow
hh3cVsanEntry = _Hh3cVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1)
)
hh3cVsanEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanEntry.setStatus("current")
_Hh3cVsanIndex_Type = Hh3cFcVsanIndex
_Hh3cVsanIndex_Object = MibTableColumn
hh3cVsanIndex = _Hh3cVsanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 1),
    _Hh3cVsanIndex_Type()
)
hh3cVsanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVsanIndex.setStatus("current")


class _Hh3cVsanCoreSwitchName_Type(Hh3cFcNameIdOrZero):
    """Custom type hh3cVsanCoreSwitchName based on Hh3cFcNameIdOrZero"""
    subtypeSpec = Hh3cFcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
    )


_Hh3cVsanCoreSwitchName_Type.__name__ = "Hh3cFcNameIdOrZero"
_Hh3cVsanCoreSwitchName_Object = MibTableColumn
hh3cVsanCoreSwitchName = _Hh3cVsanCoreSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 2),
    _Hh3cVsanCoreSwitchName_Type()
)
hh3cVsanCoreSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanCoreSwitchName.setStatus("current")
_Hh3cVsanRowStatus_Type = RowStatus
_Hh3cVsanRowStatus_Object = MibTableColumn
hh3cVsanRowStatus = _Hh3cVsanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 3),
    _Hh3cVsanRowStatus_Type()
)
hh3cVsanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsanRowStatus.setStatus("current")


class _Hh3cVsanName_Type(SnmpAdminString):
    """Custom type hh3cVsanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cVsanName_Type.__name__ = "SnmpAdminString"
_Hh3cVsanName_Object = MibTableColumn
hh3cVsanName = _Hh3cVsanName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 4),
    _Hh3cVsanName_Type()
)
hh3cVsanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsanName.setStatus("current")
_Hh3cVsanWorkingMode_Type = Integer32
_Hh3cVsanWorkingMode_Object = MibTableColumn
hh3cVsanWorkingMode = _Hh3cVsanWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 1, 1, 5),
    _Hh3cVsanWorkingMode_Type()
)
hh3cVsanWorkingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsanWorkingMode.setStatus("current")
_Hh3cVsanDmTable_Object = MibTable
hh3cVsanDmTable = _Hh3cVsanDmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cVsanDmTable.setStatus("current")
_Hh3cVsanDmEntry_Object = MibTableRow
hh3cVsanDmEntry = _Hh3cVsanDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1)
)
hh3cVsanDmEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmEntry.setStatus("current")


class _Hh3cVsanDmDomainConfigureEnable_Type(TruthValue):
    """Custom type hh3cVsanDmDomainConfigureEnable based on TruthValue"""
    defaultValue = 1


_Hh3cVsanDmDomainConfigureEnable_Type.__name__ = "TruthValue"
_Hh3cVsanDmDomainConfigureEnable_Object = MibTableColumn
hh3cVsanDmDomainConfigureEnable = _Hh3cVsanDmDomainConfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 1),
    _Hh3cVsanDmDomainConfigureEnable_Type()
)
hh3cVsanDmDomainConfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainConfigureEnable.setStatus("current")
_Hh3cVsanDmFabricNameConfigured_Type = Hh3cFcNameIdOrZero
_Hh3cVsanDmFabricNameConfigured_Object = MibTableColumn
hh3cVsanDmFabricNameConfigured = _Hh3cVsanDmFabricNameConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 2),
    _Hh3cVsanDmFabricNameConfigured_Type()
)
hh3cVsanDmFabricNameConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmFabricNameConfigured.setStatus("current")


class _Hh3cVsanDmPriorityConfigured_Type(Hh3cFcDomainPriority):
    """Custom type hh3cVsanDmPriorityConfigured based on Hh3cFcDomainPriority"""
    defaultValue = 128


_Hh3cVsanDmPriorityConfigured_Type.__name__ = "Hh3cFcDomainPriority"
_Hh3cVsanDmPriorityConfigured_Object = MibTableColumn
hh3cVsanDmPriorityConfigured = _Hh3cVsanDmPriorityConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 3),
    _Hh3cVsanDmPriorityConfigured_Type()
)
hh3cVsanDmPriorityConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmPriorityConfigured.setStatus("current")
_Hh3cVsanDmAllowedDomainIdList_Type = Hh3cFcDomainIdList
_Hh3cVsanDmAllowedDomainIdList_Object = MibTableColumn
hh3cVsanDmAllowedDomainIdList = _Hh3cVsanDmAllowedDomainIdList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 4),
    _Hh3cVsanDmAllowedDomainIdList_Type()
)
hh3cVsanDmAllowedDomainIdList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmAllowedDomainIdList.setStatus("current")


class _Hh3cVsanDmDomainIdConfigured_Type(Hh3cFcDomainIdOrZero):
    """Custom type hh3cVsanDmDomainIdConfigured based on Hh3cFcDomainIdOrZero"""
    defaultValue = 0


_Hh3cVsanDmDomainIdConfigured_Type.__name__ = "Hh3cFcDomainIdOrZero"
_Hh3cVsanDmDomainIdConfigured_Object = MibTableColumn
hh3cVsanDmDomainIdConfigured = _Hh3cVsanDmDomainIdConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 5),
    _Hh3cVsanDmDomainIdConfigured_Type()
)
hh3cVsanDmDomainIdConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdConfigured.setStatus("current")


class _Hh3cVsanDmDomainIdTypeConfigured_Type(Integer32):
    """Custom type hh3cVsanDmDomainIdTypeConfigured based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("preferred", 2))
    )


_Hh3cVsanDmDomainIdTypeConfigured_Type.__name__ = "Integer32"
_Hh3cVsanDmDomainIdTypeConfigured_Object = MibTableColumn
hh3cVsanDmDomainIdTypeConfigured = _Hh3cVsanDmDomainIdTypeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 6),
    _Hh3cVsanDmDomainIdTypeConfigured_Type()
)
hh3cVsanDmDomainIdTypeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdTypeConfigured.setStatus("current")


class _Hh3cVsanDmAutoReconfigureEnable_Type(TruthValue):
    """Custom type hh3cVsanDmAutoReconfigureEnable based on TruthValue"""
    defaultValue = 2


_Hh3cVsanDmAutoReconfigureEnable_Type.__name__ = "TruthValue"
_Hh3cVsanDmAutoReconfigureEnable_Object = MibTableColumn
hh3cVsanDmAutoReconfigureEnable = _Hh3cVsanDmAutoReconfigureEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 7),
    _Hh3cVsanDmAutoReconfigureEnable_Type()
)
hh3cVsanDmAutoReconfigureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmAutoReconfigureEnable.setStatus("current")


class _Hh3cVsanDmDomainRestart_Type(Integer32):
    """Custom type hh3cVsanDmDomainRestart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("nonDisruptive", 2),
          ("disruptive", 3))
    )


_Hh3cVsanDmDomainRestart_Type.__name__ = "Integer32"
_Hh3cVsanDmDomainRestart_Object = MibTableColumn
hh3cVsanDmDomainRestart = _Hh3cVsanDmDomainRestart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 8),
    _Hh3cVsanDmDomainRestart_Type()
)
hh3cVsanDmDomainRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainRestart.setStatus("current")
_Hh3cVsanDmState_Type = Hh3cFcDmState
_Hh3cVsanDmState_Object = MibTableColumn
hh3cVsanDmState = _Hh3cVsanDmState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 9),
    _Hh3cVsanDmState_Type()
)
hh3cVsanDmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmState.setStatus("current")
_Hh3cVsanDmDomainIdAssigned_Type = Hh3cFcDomainIdOrZero
_Hh3cVsanDmDomainIdAssigned_Object = MibTableColumn
hh3cVsanDmDomainIdAssigned = _Hh3cVsanDmDomainIdAssigned_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 10),
    _Hh3cVsanDmDomainIdAssigned_Type()
)
hh3cVsanDmDomainIdAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdAssigned.setStatus("current")
_Hh3cVsanDmPrincipalSwitchWWN_Type = Hh3cFcNameId
_Hh3cVsanDmPrincipalSwitchWWN_Object = MibTableColumn
hh3cVsanDmPrincipalSwitchWWN = _Hh3cVsanDmPrincipalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 11),
    _Hh3cVsanDmPrincipalSwitchWWN_Type()
)
hh3cVsanDmPrincipalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmPrincipalSwitchWWN.setStatus("current")
_Hh3cVsanDmLocalSwitchWWN_Type = Hh3cFcNameId
_Hh3cVsanDmLocalSwitchWWN_Object = MibTableColumn
hh3cVsanDmLocalSwitchWWN = _Hh3cVsanDmLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 12),
    _Hh3cVsanDmLocalSwitchWWN_Type()
)
hh3cVsanDmLocalSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmLocalSwitchWWN.setStatus("current")
_Hh3cVsanDmPrincipalSwRunPriority_Type = Hh3cFcDomainPriority
_Hh3cVsanDmPrincipalSwRunPriority_Object = MibTableColumn
hh3cVsanDmPrincipalSwRunPriority = _Hh3cVsanDmPrincipalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 13),
    _Hh3cVsanDmPrincipalSwRunPriority_Type()
)
hh3cVsanDmPrincipalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmPrincipalSwRunPriority.setStatus("current")
_Hh3cVsanDmLocalSwRunPriority_Type = Hh3cFcDomainPriority
_Hh3cVsanDmLocalSwRunPriority_Object = MibTableColumn
hh3cVsanDmLocalSwRunPriority = _Hh3cVsanDmLocalSwRunPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 14),
    _Hh3cVsanDmLocalSwRunPriority_Type()
)
hh3cVsanDmLocalSwRunPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmLocalSwRunPriority.setStatus("current")
_Hh3cVsanDmPrincipalSwSlctCnt_Type = Counter32
_Hh3cVsanDmPrincipalSwSlctCnt_Object = MibTableColumn
hh3cVsanDmPrincipalSwSlctCnt = _Hh3cVsanDmPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 15),
    _Hh3cVsanDmPrincipalSwSlctCnt_Type()
)
hh3cVsanDmPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmPrincipalSwSlctCnt.setStatus("current")
_Hh3cVsanDmLocalPrincipalSwSlctCnt_Type = Counter32
_Hh3cVsanDmLocalPrincipalSwSlctCnt_Object = MibTableColumn
hh3cVsanDmLocalPrincipalSwSlctCnt = _Hh3cVsanDmLocalPrincipalSwSlctCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 16),
    _Hh3cVsanDmLocalPrincipalSwSlctCnt_Type()
)
hh3cVsanDmLocalPrincipalSwSlctCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmLocalPrincipalSwSlctCnt.setStatus("current")
_Hh3cVsanDmBFCnt_Type = Counter32
_Hh3cVsanDmBFCnt_Object = MibTableColumn
hh3cVsanDmBFCnt = _Hh3cVsanDmBFCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 17),
    _Hh3cVsanDmBFCnt_Type()
)
hh3cVsanDmBFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmBFCnt.setStatus("current")
_Hh3cVsanDmRCFCnt_Type = Counter32
_Hh3cVsanDmRCFCnt_Object = MibTableColumn
hh3cVsanDmRCFCnt = _Hh3cVsanDmRCFCnt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 2, 1, 18),
    _Hh3cVsanDmRCFCnt_Type()
)
hh3cVsanDmRCFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmRCFCnt.setStatus("current")
_Hh3cVsanDmIfConfigTable_Object = MibTable
hh3cVsanDmIfConfigTable = _Hh3cVsanDmIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfConfigTable.setStatus("current")
_Hh3cVsanDmIfConfigEntry_Object = MibTableRow
hh3cVsanDmIfConfigEntry = _Hh3cVsanDmIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 3, 1)
)
hh3cVsanDmIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfConfigEntry.setStatus("current")


class _Hh3cVsanDmIfConfigRcfReject_Type(TruthValue):
    """Custom type hh3cVsanDmIfConfigRcfReject based on TruthValue"""
    defaultValue = 2


_Hh3cVsanDmIfConfigRcfReject_Type.__name__ = "TruthValue"
_Hh3cVsanDmIfConfigRcfReject_Object = MibTableColumn
hh3cVsanDmIfConfigRcfReject = _Hh3cVsanDmIfConfigRcfReject_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 3, 1, 1),
    _Hh3cVsanDmIfConfigRcfReject_Type()
)
hh3cVsanDmIfConfigRcfReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmIfConfigRcfReject.setStatus("current")
_Hh3cVsanFcIdTable_Object = MibTable
hh3cVsanFcIdTable = _Hh3cVsanFcIdTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cVsanFcIdTable.setStatus("current")
_Hh3cVsanFcIdEntry_Object = MibTableRow
hh3cVsanFcIdEntry = _Hh3cVsanFcIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 4, 1)
)
hh3cVsanFcIdEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanFcIdEntry.setStatus("current")
_Hh3cVsanFreeFcIds_Type = Counter32
_Hh3cVsanFreeFcIds_Object = MibTableColumn
hh3cVsanFreeFcIds = _Hh3cVsanFreeFcIds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 4, 1, 1),
    _Hh3cVsanFreeFcIds_Type()
)
hh3cVsanFreeFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanFreeFcIds.setStatus("current")
_Hh3cVsanAssignedFcIds_Type = Counter32
_Hh3cVsanAssignedFcIds_Object = MibTableColumn
hh3cVsanAssignedFcIds = _Hh3cVsanAssignedFcIds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 4, 1, 2),
    _Hh3cVsanAssignedFcIds_Type()
)
hh3cVsanAssignedFcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanAssignedFcIds.setStatus("current")


class _Hh3cVsanFcIdPersistency_Type(TruthValue):
    """Custom type hh3cVsanFcIdPersistency based on TruthValue"""
    defaultValue = 1


_Hh3cVsanFcIdPersistency_Type.__name__ = "TruthValue"
_Hh3cVsanFcIdPersistency_Object = MibTableColumn
hh3cVsanFcIdPersistency = _Hh3cVsanFcIdPersistency_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 4, 1, 3),
    _Hh3cVsanFcIdPersistency_Type()
)
hh3cVsanFcIdPersistency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistency.setStatus("current")


class _Hh3cVsanFcIdPurge_Type(Integer32):
    """Custom type hh3cVsanFcIdPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("enable", 2))
    )


_Hh3cVsanFcIdPurge_Type.__name__ = "Integer32"
_Hh3cVsanFcIdPurge_Object = MibTableColumn
hh3cVsanFcIdPurge = _Hh3cVsanFcIdPurge_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 4, 1, 4),
    _Hh3cVsanFcIdPurge_Type()
)
hh3cVsanFcIdPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanFcIdPurge.setStatus("current")
_Hh3cVsanFcIdPersistencyTable_Object = MibTable
hh3cVsanFcIdPersistencyTable = _Hh3cVsanFcIdPersistencyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistencyTable.setStatus("current")
_Hh3cVsanFcIdPersistencyEntry_Object = MibTableRow
hh3cVsanFcIdPersistencyEntry = _Hh3cVsanFcIdPersistencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 5, 1)
)
hh3cVsanFcIdPersistencyEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanFcIdPersistencyWwn"),
)
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistencyEntry.setStatus("current")
_Hh3cVsanFcIdPersistencyWwn_Type = Hh3cFcNameId
_Hh3cVsanFcIdPersistencyWwn_Object = MibTableColumn
hh3cVsanFcIdPersistencyWwn = _Hh3cVsanFcIdPersistencyWwn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 5, 1, 1),
    _Hh3cVsanFcIdPersistencyWwn_Type()
)
hh3cVsanFcIdPersistencyWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistencyWwn.setStatus("current")
_Hh3cVsanFcIdPersistencyFcId_Type = Hh3cFcAddressId
_Hh3cVsanFcIdPersistencyFcId_Object = MibTableColumn
hh3cVsanFcIdPersistencyFcId = _Hh3cVsanFcIdPersistencyFcId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 5, 1, 2),
    _Hh3cVsanFcIdPersistencyFcId_Type()
)
hh3cVsanFcIdPersistencyFcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistencyFcId.setStatus("current")
_Hh3cVsanFcIdPersistencyUsed_Type = TruthValue
_Hh3cVsanFcIdPersistencyUsed_Object = MibTableColumn
hh3cVsanFcIdPersistencyUsed = _Hh3cVsanFcIdPersistencyUsed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 5, 1, 3),
    _Hh3cVsanFcIdPersistencyUsed_Type()
)
hh3cVsanFcIdPersistencyUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistencyUsed.setStatus("current")


class _Hh3cVsanFcIdPersistencyType_Type(Integer32):
    """Custom type hh3cVsanFcIdPersistencyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_Hh3cVsanFcIdPersistencyType_Type.__name__ = "Integer32"
_Hh3cVsanFcIdPersistencyType_Object = MibTableColumn
hh3cVsanFcIdPersistencyType = _Hh3cVsanFcIdPersistencyType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 5, 1, 4),
    _Hh3cVsanFcIdPersistencyType_Type()
)
hh3cVsanFcIdPersistencyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistencyType.setStatus("current")
_Hh3cVsanFcIdPersistencyRowStatus_Type = RowStatus
_Hh3cVsanFcIdPersistencyRowStatus_Object = MibTableColumn
hh3cVsanFcIdPersistencyRowStatus = _Hh3cVsanFcIdPersistencyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 1, 5, 1, 5),
    _Hh3cVsanFcIdPersistencyRowStatus_Type()
)
hh3cVsanFcIdPersistencyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cVsanFcIdPersistencyRowStatus.setStatus("current")
_Hh3cVsanDmInformation_ObjectIdentity = ObjectIdentity
hh3cVsanDmInformation = _Hh3cVsanDmInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2)
)
_Hh3cVsanDmDatabaseTable_Object = MibTable
hh3cVsanDmDatabaseTable = _Hh3cVsanDmDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseTable.setStatus("current")
_Hh3cVsanDmDatabaseEntry_Object = MibTableRow
hh3cVsanDmDatabaseEntry = _Hh3cVsanDmDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1, 1)
)
hh3cVsanDmDatabaseEntry.setIndexNames(
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanDmDatabaseDomainId"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseEntry.setStatus("current")
_Hh3cVsanDmDatabaseDomainId_Type = Hh3cFcDomainId
_Hh3cVsanDmDatabaseDomainId_Object = MibTableColumn
hh3cVsanDmDatabaseDomainId = _Hh3cVsanDmDatabaseDomainId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1, 1, 1),
    _Hh3cVsanDmDatabaseDomainId_Type()
)
hh3cVsanDmDatabaseDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseDomainId.setStatus("current")
_Hh3cVsanDmDatabaseSwitchWWN_Type = Hh3cFcNameId
_Hh3cVsanDmDatabaseSwitchWWN_Object = MibTableColumn
hh3cVsanDmDatabaseSwitchWWN = _Hh3cVsanDmDatabaseSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 1, 1, 2),
    _Hh3cVsanDmDatabaseSwitchWWN_Type()
)
hh3cVsanDmDatabaseSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmDatabaseSwitchWWN.setStatus("current")
_Hh3cVsanDmIfInfoTable_Object = MibTable
hh3cVsanDmIfInfoTable = _Hh3cVsanDmIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfInfoTable.setStatus("current")
_Hh3cVsanDmIfInfoEntry_Object = MibTableRow
hh3cVsanDmIfInfoEntry = _Hh3cVsanDmIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 2, 1)
)
hh3cVsanDmIfInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-VSAN-MIB", "hh3cVsanIndex"),
)
if mibBuilder.loadTexts:
    hh3cVsanDmIfInfoEntry.setStatus("current")


class _Hh3cVsanDmIfInfoRole_Type(Integer32):
    """Custom type hh3cVsanDmIfInfoRole based on Integer32"""
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
        *(("nonPrincipal", 1),
          ("principalUpstream", 2),
          ("principalDownstream", 3),
          ("isolated", 4),
          ("unknown", 5))
    )


_Hh3cVsanDmIfInfoRole_Type.__name__ = "Integer32"
_Hh3cVsanDmIfInfoRole_Object = MibTableColumn
hh3cVsanDmIfInfoRole = _Hh3cVsanDmIfInfoRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 2, 2, 1, 1),
    _Hh3cVsanDmIfInfoRole_Type()
)
hh3cVsanDmIfInfoRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVsanDmIfInfoRole.setStatus("current")
_Hh3cVsanDmNotifications_ObjectIdentity = ObjectIdentity
hh3cVsanDmNotifications = _Hh3cVsanDmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3)
)
_Hh3cVsanDmNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cVsanDmNotificationPrefix = _Hh3cVsanDmNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0)
)
_Hh3cVsanDmNotificationSwitch_ObjectIdentity = ObjectIdentity
hh3cVsanDmNotificationSwitch = _Hh3cVsanDmNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 1)
)


class _Hh3cVsanDmFabricChangeNotifyEnable_Type(TruthValue):
    """Custom type hh3cVsanDmFabricChangeNotifyEnable based on TruthValue"""
    defaultValue = 2


_Hh3cVsanDmFabricChangeNotifyEnable_Type.__name__ = "TruthValue"
_Hh3cVsanDmFabricChangeNotifyEnable_Object = MibScalar
hh3cVsanDmFabricChangeNotifyEnable = _Hh3cVsanDmFabricChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 1, 1),
    _Hh3cVsanDmFabricChangeNotifyEnable_Type()
)
hh3cVsanDmFabricChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmFabricChangeNotifyEnable.setStatus("current")


class _Hh3cVsanDmDomainIdChangeNotifyEnable_Type(TruthValue):
    """Custom type hh3cVsanDmDomainIdChangeNotifyEnable based on TruthValue"""
    defaultValue = 2


_Hh3cVsanDmDomainIdChangeNotifyEnable_Type.__name__ = "TruthValue"
_Hh3cVsanDmDomainIdChangeNotifyEnable_Object = MibScalar
hh3cVsanDmDomainIdChangeNotifyEnable = _Hh3cVsanDmDomainIdChangeNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 1, 2),
    _Hh3cVsanDmDomainIdChangeNotifyEnable_Type()
)
hh3cVsanDmDomainIdChangeNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdChangeNotifyEnable.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cVsanDmDomainIdNotAssignedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 1)
)
hh3cVsanDmDomainIdNotAssignedNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdNotAssignedNotify.setStatus(
        "current"
    )

hh3cVsanDmNewPrincipalSwitchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 2)
)
hh3cVsanDmNewPrincipalSwitchNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hh3cVsanDmNewPrincipalSwitchNotify.setStatus(
        "current"
    )

hh3cVsanDmFabricChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 3)
)
hh3cVsanDmFabricChangeNotify.setObjects(
    ("HH3C-VSAN-MIB", "hh3cVsanIndex")
)
if mibBuilder.loadTexts:
    hh3cVsanDmFabricChangeNotify.setStatus(
        "current"
    )

hh3cVsanDmDomainIdChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 127, 1, 1, 3, 0, 4)
)
hh3cVsanDmDomainIdChangeNotify.setObjects(
      *(("HH3C-VSAN-MIB", "hh3cVsanIndex"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmDomainIdAssigned"),
        ("HH3C-VSAN-MIB", "hh3cVsanDmLocalSwitchWWN"))
)
if mibBuilder.loadTexts:
    hh3cVsanDmDomainIdChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VSAN-MIB",
    **{"hh3cSan": hh3cSan,
       "hh3cVsan": hh3cVsan,
       "hh3cVsanMibObjects": hh3cVsanMibObjects,
       "hh3cVsanDmConfiguration": hh3cVsanDmConfiguration,
       "hh3cVsanTable": hh3cVsanTable,
       "hh3cVsanEntry": hh3cVsanEntry,
       "hh3cVsanIndex": hh3cVsanIndex,
       "hh3cVsanCoreSwitchName": hh3cVsanCoreSwitchName,
       "hh3cVsanRowStatus": hh3cVsanRowStatus,
       "hh3cVsanName": hh3cVsanName,
       "hh3cVsanWorkingMode": hh3cVsanWorkingMode,
       "hh3cVsanDmTable": hh3cVsanDmTable,
       "hh3cVsanDmEntry": hh3cVsanDmEntry,
       "hh3cVsanDmDomainConfigureEnable": hh3cVsanDmDomainConfigureEnable,
       "hh3cVsanDmFabricNameConfigured": hh3cVsanDmFabricNameConfigured,
       "hh3cVsanDmPriorityConfigured": hh3cVsanDmPriorityConfigured,
       "hh3cVsanDmAllowedDomainIdList": hh3cVsanDmAllowedDomainIdList,
       "hh3cVsanDmDomainIdConfigured": hh3cVsanDmDomainIdConfigured,
       "hh3cVsanDmDomainIdTypeConfigured": hh3cVsanDmDomainIdTypeConfigured,
       "hh3cVsanDmAutoReconfigureEnable": hh3cVsanDmAutoReconfigureEnable,
       "hh3cVsanDmDomainRestart": hh3cVsanDmDomainRestart,
       "hh3cVsanDmState": hh3cVsanDmState,
       "hh3cVsanDmDomainIdAssigned": hh3cVsanDmDomainIdAssigned,
       "hh3cVsanDmPrincipalSwitchWWN": hh3cVsanDmPrincipalSwitchWWN,
       "hh3cVsanDmLocalSwitchWWN": hh3cVsanDmLocalSwitchWWN,
       "hh3cVsanDmPrincipalSwRunPriority": hh3cVsanDmPrincipalSwRunPriority,
       "hh3cVsanDmLocalSwRunPriority": hh3cVsanDmLocalSwRunPriority,
       "hh3cVsanDmPrincipalSwSlctCnt": hh3cVsanDmPrincipalSwSlctCnt,
       "hh3cVsanDmLocalPrincipalSwSlctCnt": hh3cVsanDmLocalPrincipalSwSlctCnt,
       "hh3cVsanDmBFCnt": hh3cVsanDmBFCnt,
       "hh3cVsanDmRCFCnt": hh3cVsanDmRCFCnt,
       "hh3cVsanDmIfConfigTable": hh3cVsanDmIfConfigTable,
       "hh3cVsanDmIfConfigEntry": hh3cVsanDmIfConfigEntry,
       "hh3cVsanDmIfConfigRcfReject": hh3cVsanDmIfConfigRcfReject,
       "hh3cVsanFcIdTable": hh3cVsanFcIdTable,
       "hh3cVsanFcIdEntry": hh3cVsanFcIdEntry,
       "hh3cVsanFreeFcIds": hh3cVsanFreeFcIds,
       "hh3cVsanAssignedFcIds": hh3cVsanAssignedFcIds,
       "hh3cVsanFcIdPersistency": hh3cVsanFcIdPersistency,
       "hh3cVsanFcIdPurge": hh3cVsanFcIdPurge,
       "hh3cVsanFcIdPersistencyTable": hh3cVsanFcIdPersistencyTable,
       "hh3cVsanFcIdPersistencyEntry": hh3cVsanFcIdPersistencyEntry,
       "hh3cVsanFcIdPersistencyWwn": hh3cVsanFcIdPersistencyWwn,
       "hh3cVsanFcIdPersistencyFcId": hh3cVsanFcIdPersistencyFcId,
       "hh3cVsanFcIdPersistencyUsed": hh3cVsanFcIdPersistencyUsed,
       "hh3cVsanFcIdPersistencyType": hh3cVsanFcIdPersistencyType,
       "hh3cVsanFcIdPersistencyRowStatus": hh3cVsanFcIdPersistencyRowStatus,
       "hh3cVsanDmInformation": hh3cVsanDmInformation,
       "hh3cVsanDmDatabaseTable": hh3cVsanDmDatabaseTable,
       "hh3cVsanDmDatabaseEntry": hh3cVsanDmDatabaseEntry,
       "hh3cVsanDmDatabaseDomainId": hh3cVsanDmDatabaseDomainId,
       "hh3cVsanDmDatabaseSwitchWWN": hh3cVsanDmDatabaseSwitchWWN,
       "hh3cVsanDmIfInfoTable": hh3cVsanDmIfInfoTable,
       "hh3cVsanDmIfInfoEntry": hh3cVsanDmIfInfoEntry,
       "hh3cVsanDmIfInfoRole": hh3cVsanDmIfInfoRole,
       "hh3cVsanDmNotifications": hh3cVsanDmNotifications,
       "hh3cVsanDmNotificationPrefix": hh3cVsanDmNotificationPrefix,
       "hh3cVsanDmDomainIdNotAssignedNotify": hh3cVsanDmDomainIdNotAssignedNotify,
       "hh3cVsanDmNewPrincipalSwitchNotify": hh3cVsanDmNewPrincipalSwitchNotify,
       "hh3cVsanDmFabricChangeNotify": hh3cVsanDmFabricChangeNotify,
       "hh3cVsanDmDomainIdChangeNotify": hh3cVsanDmDomainIdChangeNotify,
       "hh3cVsanDmNotificationSwitch": hh3cVsanDmNotificationSwitch,
       "hh3cVsanDmFabricChangeNotifyEnable": hh3cVsanDmFabricChangeNotifyEnable,
       "hh3cVsanDmDomainIdChangeNotifyEnable": hh3cVsanDmDomainIdChangeNotifyEnable}
)
