# SNMP MIB module (XF-SOFTWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\XF-SOFTWARE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:51 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(XfProductRevision,
 XfProductnumber,
 xfPlatform) = mibBuilder.importSymbols(
    "XF-TOP-MIB",
    "XfProductRevision",
    "XfProductnumber",
    "xfPlatform")


# MODULE-IDENTITY

xfSoftwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7)
)
if mibBuilder.loadTexts:
    xfSoftwareMIB.setRevisions(
        ("2008-03-05 18:03",
         "2007-11-26 12:44",
         "2007-06-11 09:12",
         "2007-04-10 09:09",
         "2003-06-19 10:30",
         "2002-03-08 08:41",
         "2002-01-14 09:11",
         "2001-10-10 12:15",
         "2004-01-30 13:51",
         "2004-08-03 08:23",
         "2005-01-31 08:26",
         "2005-02-09 08:13")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class XfSwRelease(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class XfSwEnableDisable(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_XfSwObjects_ObjectIdentity = ObjectIdentity
xfSwObjects = _XfSwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1)
)
_XfSwLoadModuleTable_Object = MibTable
xfSwLoadModuleTable = _XfSwLoadModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    xfSwLoadModuleTable.setStatus("current")
_XfSwLoadModuleEntry_Object = MibTableRow
xfSwLoadModuleEntry = _XfSwLoadModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1)
)
xfSwLoadModuleEntry.setIndexNames(
    (0, "XF-SOFTWARE-MIB", "xfSwRelease"),
    (0, "XF-SOFTWARE-MIB", "xfSwLoadModuleIndex"),
)
if mibBuilder.loadTexts:
    xfSwLoadModuleEntry.setStatus("current")
_XfSwRelease_Type = XfSwRelease
_XfSwRelease_Object = MibTableColumn
xfSwRelease = _XfSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 1),
    _XfSwRelease_Type()
)
xfSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwRelease.setStatus("current")


class _XfSwLoadModuleIndex_Type(Integer32):
    """Custom type xfSwLoadModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_XfSwLoadModuleIndex_Type.__name__ = "Integer32"
_XfSwLoadModuleIndex_Object = MibTableColumn
xfSwLoadModuleIndex = _XfSwLoadModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 2),
    _XfSwLoadModuleIndex_Type()
)
xfSwLoadModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLoadModuleIndex.setStatus("current")
_XfSwLoadModuleProductNumber_Type = XfProductnumber
_XfSwLoadModuleProductNumber_Object = MibTableColumn
xfSwLoadModuleProductNumber = _XfSwLoadModuleProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 3),
    _XfSwLoadModuleProductNumber_Type()
)
xfSwLoadModuleProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLoadModuleProductNumber.setStatus("current")
_XfSwLoadModuleRevision_Type = XfProductRevision
_XfSwLoadModuleRevision_Object = MibTableColumn
xfSwLoadModuleRevision = _XfSwLoadModuleRevision_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 4),
    _XfSwLoadModuleRevision_Type()
)
xfSwLoadModuleRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLoadModuleRevision.setStatus("current")


class _XfSwLoadModuleOperStatus_Type(Integer32):
    """Custom type xfSwLoadModuleOperStatus based on Integer32"""
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
        *(("passive", 1),
          ("upgradeStarted", 2),
          ("upgradeFinished", 3),
          ("upgradeFailed", 4),
          ("upgradeAborted", 5))
    )


_XfSwLoadModuleOperStatus_Type.__name__ = "Integer32"
_XfSwLoadModuleOperStatus_Object = MibTableColumn
xfSwLoadModuleOperStatus = _XfSwLoadModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 5),
    _XfSwLoadModuleOperStatus_Type()
)
xfSwLoadModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLoadModuleOperStatus.setStatus("current")


class _XfSwLoadModuleFailure_Type(Integer32):
    """Custom type xfSwLoadModuleFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadFailure", 1),
          ("programFailure", 2),
          ("noFailure", 3))
    )


_XfSwLoadModuleFailure_Type.__name__ = "Integer32"
_XfSwLoadModuleFailure_Object = MibTableColumn
xfSwLoadModuleFailure = _XfSwLoadModuleFailure_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 6),
    _XfSwLoadModuleFailure_Type()
)
xfSwLoadModuleFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLoadModuleFailure.setStatus("current")


class _XfSwLoadModuleProgress_Type(Integer32):
    """Custom type xfSwLoadModuleProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XfSwLoadModuleProgress_Type.__name__ = "Integer32"
_XfSwLoadModuleProgress_Object = MibTableColumn
xfSwLoadModuleProgress = _XfSwLoadModuleProgress_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 8),
    _XfSwLoadModuleProgress_Type()
)
xfSwLoadModuleProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLoadModuleProgress.setStatus("current")
if mibBuilder.loadTexts:
    xfSwLoadModuleProgress.setUnits("percent")


class _XfSwLoadModuleDescription_Type(SnmpAdminString):
    """Custom type xfSwLoadModuleDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_XfSwLoadModuleDescription_Type.__name__ = "SnmpAdminString"
_XfSwLoadModuleDescription_Object = MibTableColumn
xfSwLoadModuleDescription = _XfSwLoadModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 1, 1, 9),
    _XfSwLoadModuleDescription_Type()
)
xfSwLoadModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLoadModuleDescription.setStatus("current")
_XfSwReleaseTable_Object = MibTable
xfSwReleaseTable = _XfSwReleaseTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2)
)
if mibBuilder.loadTexts:
    xfSwReleaseTable.setStatus("current")
_XfSwReleaseEntry_Object = MibTableRow
xfSwReleaseEntry = _XfSwReleaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1)
)
xfSwReleaseEntry.setIndexNames(
    (0, "XF-SOFTWARE-MIB", "xfSwReleaseIndex"),
)
if mibBuilder.loadTexts:
    xfSwReleaseEntry.setStatus("current")
_XfSwReleaseIndex_Type = XfSwRelease
_XfSwReleaseIndex_Object = MibTableColumn
xfSwReleaseIndex = _XfSwReleaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 1),
    _XfSwReleaseIndex_Type()
)
xfSwReleaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwReleaseIndex.setStatus("current")
_XfSwReleaseProductNumber_Type = XfProductnumber
_XfSwReleaseProductNumber_Object = MibTableColumn
xfSwReleaseProductNumber = _XfSwReleaseProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 2),
    _XfSwReleaseProductNumber_Type()
)
xfSwReleaseProductNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwReleaseProductNumber.setStatus("current")
_XfSwReleaseRevision_Type = XfProductRevision
_XfSwReleaseRevision_Object = MibTableColumn
xfSwReleaseRevision = _XfSwReleaseRevision_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 3),
    _XfSwReleaseRevision_Type()
)
xfSwReleaseRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwReleaseRevision.setStatus("current")


class _XfSwReleaseAdminStatus_Type(Integer32):
    """Custom type xfSwReleaseAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("upgradeStarted", 1),
          ("upgradeAborted", 2),
          ("activeAndRunning", 5),
          ("upgradeTest", 6))
    )


_XfSwReleaseAdminStatus_Type.__name__ = "Integer32"
_XfSwReleaseAdminStatus_Object = MibTableColumn
xfSwReleaseAdminStatus = _XfSwReleaseAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 4),
    _XfSwReleaseAdminStatus_Type()
)
xfSwReleaseAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwReleaseAdminStatus.setStatus("current")


class _XfSwReleaseOperStatus_Type(Integer32):
    """Custom type xfSwReleaseOperStatus based on Integer32"""
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
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              421,
              425,
              426,
              450,
              451,
              452,
              501,
              502,
              503,
              504,
              530,
              532,
              550,
              552,
              553)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("upgradeStarted", 2),
          ("upgradeFinished", 3),
          ("testing", 4),
          ("upgradeFailed", 5),
          ("upgradeAborted", 6),
          ("running", 7),
          ("testingFromManual", 8),
          ("errorInternal", 50),
          ("errorFileStorage", 51),
          ("ftpPingFailed", 52),
          ("ftpNoAccess", 53),
          ("ftpConnectionDetailsMissing", 54),
          ("ftpConnectionDetailsInvalid", 55),
          ("ftpConnectionTimeout", 56),
          ("ftpNoSuchRemoteFile", 57),
          ("ftpNoSuchRemoteDir", 58),
          ("ftpServiceNotAvailable", 421),
          ("ftpUnableToOpenDataConnection", 425),
          ("ftpConnectionClosed", 426),
          ("ftpFileBusy", 450),
          ("ftpLocalError", 451),
          ("ftpInsufficientStorageSpace", 452),
          ("ftpSyntaxError", 501),
          ("ftpCommandNotImplemented", 502),
          ("ftpBadSequenceCommands", 503),
          ("ftpParameterNotImplemented", 504),
          ("ftpNoLoggedIn", 530),
          ("ftpNeedAccount", 532),
          ("ftpFileUnavailable", 550),
          ("ftpExceededStorageAllocation", 552),
          ("ftpFileNameNotAllowed", 553))
    )


_XfSwReleaseOperStatus_Type.__name__ = "Integer32"
_XfSwReleaseOperStatus_Object = MibTableColumn
xfSwReleaseOperStatus = _XfSwReleaseOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 5),
    _XfSwReleaseOperStatus_Type()
)
xfSwReleaseOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwReleaseOperStatus.setStatus("current")


class _XfSwReleaseSBLType_Type(Integer32):
    """Custom type xfSwReleaseSBLType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("definedByEricsson", 1),
          ("definedByOperator", 2))
    )


_XfSwReleaseSBLType_Type.__name__ = "Integer32"
_XfSwReleaseSBLType_Object = MibTableColumn
xfSwReleaseSBLType = _XfSwReleaseSBLType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 2, 1, 6),
    _XfSwReleaseSBLType_Type()
)
xfSwReleaseSBLType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwReleaseSBLType.setStatus("current")
_XfSwActiveRelease_Type = XfSwRelease
_XfSwActiveRelease_Object = MibScalar
xfSwActiveRelease = _XfSwActiveRelease_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 3),
    _XfSwActiveRelease_Type()
)
xfSwActiveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwActiveRelease.setStatus("current")
_XfSwBootTime_Type = DateAndTime
_XfSwBootTime_Object = MibScalar
xfSwBootTime = _XfSwBootTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 4),
    _XfSwBootTime_Type()
)
xfSwBootTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwBootTime.setStatus("current")


class _XfSwCommitType_Type(Integer32):
    """Custom type xfSwCommitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operatorCommit", 1),
          ("nodeCommit", 2))
    )


_XfSwCommitType_Type.__name__ = "Integer32"
_XfSwCommitType_Object = MibScalar
xfSwCommitType = _XfSwCommitType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 5),
    _XfSwCommitType_Type()
)
xfSwCommitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwCommitType.setStatus("current")
_XfSwBoardTable_Object = MibTable
xfSwBoardTable = _XfSwBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    xfSwBoardTable.setStatus("current")
_XfSwBoardEntry_Object = MibTableRow
xfSwBoardEntry = _XfSwBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1)
)
xfSwBoardEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "XF-SOFTWARE-MIB", "xfSwLoadModuleIndex"),
)
if mibBuilder.loadTexts:
    xfSwBoardEntry.setStatus("current")


class _XfSwBoardLoadModuleIndex_Type(Integer32):
    """Custom type xfSwBoardLoadModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XfSwBoardLoadModuleIndex_Type.__name__ = "Integer32"
_XfSwBoardLoadModuleIndex_Object = MibTableColumn
xfSwBoardLoadModuleIndex = _XfSwBoardLoadModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 1),
    _XfSwBoardLoadModuleIndex_Type()
)
xfSwBoardLoadModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardLoadModuleIndex.setStatus("current")
_XfSwBoardLoadModuleType_Type = ObjectIdentifier
_XfSwBoardLoadModuleType_Object = MibTableColumn
xfSwBoardLoadModuleType = _XfSwBoardLoadModuleType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 2),
    _XfSwBoardLoadModuleType_Type()
)
xfSwBoardLoadModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardLoadModuleType.setStatus("obsolete")
_XfSwBoardProductNumber_Type = XfProductnumber
_XfSwBoardProductNumber_Object = MibTableColumn
xfSwBoardProductNumber = _XfSwBoardProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 3),
    _XfSwBoardProductNumber_Type()
)
xfSwBoardProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardProductNumber.setStatus("current")
_XfSwBoardRevision_Type = XfProductRevision
_XfSwBoardRevision_Object = MibTableColumn
xfSwBoardRevision = _XfSwBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 4),
    _XfSwBoardRevision_Type()
)
xfSwBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardRevision.setStatus("current")


class _XfSwBoardStatus_Type(Integer32):
    """Custom type xfSwBoardStatus based on Integer32"""
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
        *(("unknown", 1),
          ("active", 2),
          ("upgrading", 3),
          ("wrongSoftware", 4),
          ("minSoftwareRevision", 5))
    )


_XfSwBoardStatus_Type.__name__ = "Integer32"
_XfSwBoardStatus_Object = MibTableColumn
xfSwBoardStatus = _XfSwBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 5),
    _XfSwBoardStatus_Type()
)
xfSwBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardStatus.setStatus("current")


class _XfSwBoardSuProgress_Type(Integer32):
    """Custom type xfSwBoardSuProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XfSwBoardSuProgress_Type.__name__ = "Integer32"
_XfSwBoardSuProgress_Object = MibTableColumn
xfSwBoardSuProgress = _XfSwBoardSuProgress_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 6),
    _XfSwBoardSuProgress_Type()
)
xfSwBoardSuProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardSuProgress.setStatus("current")
if mibBuilder.loadTexts:
    xfSwBoardSuProgress.setUnits("percent")
_XfSwBoardMinProductNumber_Type = XfProductnumber
_XfSwBoardMinProductNumber_Object = MibTableColumn
xfSwBoardMinProductNumber = _XfSwBoardMinProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 7),
    _XfSwBoardMinProductNumber_Type()
)
xfSwBoardMinProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardMinProductNumber.setStatus("current")
_XfSwBoardMinRevision_Type = XfProductRevision
_XfSwBoardMinRevision_Object = MibTableColumn
xfSwBoardMinRevision = _XfSwBoardMinRevision_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 8),
    _XfSwBoardMinRevision_Type()
)
xfSwBoardMinRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardMinRevision.setStatus("current")


class _XfSwBoardTrafficDisturbance_Type(Integer32):
    """Custom type xfSwBoardTrafficDisturbance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disturbing", 2),
          ("notDisturbing", 3))
    )


_XfSwBoardTrafficDisturbance_Type.__name__ = "Integer32"
_XfSwBoardTrafficDisturbance_Object = MibTableColumn
xfSwBoardTrafficDisturbance = _XfSwBoardTrafficDisturbance_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 6, 1, 9),
    _XfSwBoardTrafficDisturbance_Type()
)
xfSwBoardTrafficDisturbance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwBoardTrafficDisturbance.setStatus("current")
_XfSwNpuObjects_ObjectIdentity = ObjectIdentity
xfSwNpuObjects = _XfSwNpuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7)
)
_XfSwNpuPassiveProductNumber_Type = XfProductnumber
_XfSwNpuPassiveProductNumber_Object = MibScalar
xfSwNpuPassiveProductNumber = _XfSwNpuPassiveProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7, 1),
    _XfSwNpuPassiveProductNumber_Type()
)
xfSwNpuPassiveProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwNpuPassiveProductNumber.setStatus("current")
_XfSwNpuPassiveRevision_Type = XfProductRevision
_XfSwNpuPassiveRevision_Object = MibScalar
xfSwNpuPassiveRevision = _XfSwNpuPassiveRevision_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7, 2),
    _XfSwNpuPassiveRevision_Type()
)
xfSwNpuPassiveRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwNpuPassiveRevision.setStatus("current")


class _XfSwNpuPassiveSwitch_Type(Integer32):
    """Custom type xfSwNpuPassiveSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("switch", 1)
    )


_XfSwNpuPassiveSwitch_Type.__name__ = "Integer32"
_XfSwNpuPassiveSwitch_Object = MibScalar
xfSwNpuPassiveSwitch = _XfSwNpuPassiveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 7, 3),
    _XfSwNpuPassiveSwitch_Type()
)
xfSwNpuPassiveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwNpuPassiveSwitch.setStatus("current")
_XfSwLoadModuleTypes_ObjectIdentity = ObjectIdentity
xfSwLoadModuleTypes = _XfSwLoadModuleTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 8)
)
_XfDeviceProcessorSoftware_ObjectIdentity = ObjectIdentity
xfDeviceProcessorSoftware = _XfDeviceProcessorSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 8, 1)
)
if mibBuilder.loadTexts:
    xfDeviceProcessorSoftware.setStatus("obsolete")
_XfPciFpgaCode_ObjectIdentity = ObjectIdentity
xfPciFpgaCode = _XfPciFpgaCode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 8, 2)
)
if mibBuilder.loadTexts:
    xfPciFpgaCode.setStatus("obsolete")
_XfSwUpgradePreferences_ObjectIdentity = ObjectIdentity
xfSwUpgradePreferences = _XfSwUpgradePreferences_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9)
)
_XfSwVersionControl_Type = XfSwEnableDisable
_XfSwVersionControl_Object = MibScalar
xfSwVersionControl = _XfSwVersionControl_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 1),
    _XfSwVersionControl_Type()
)
xfSwVersionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwVersionControl.setStatus("current")
_XfSwAutoUpgrade_Type = XfSwEnableDisable
_XfSwAutoUpgrade_Object = MibScalar
xfSwAutoUpgrade = _XfSwAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 2),
    _XfSwAutoUpgrade_Type()
)
xfSwAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwAutoUpgrade.setStatus("current")
_XfSwAutoDowngrade_Type = XfSwEnableDisable
_XfSwAutoDowngrade_Object = MibScalar
xfSwAutoDowngrade = _XfSwAutoDowngrade_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 3),
    _XfSwAutoDowngrade_Type()
)
xfSwAutoDowngrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwAutoDowngrade.setStatus("current")
_XfSwAcceptFailure_Type = XfSwEnableDisable
_XfSwAcceptFailure_Object = MibScalar
xfSwAcceptFailure = _XfSwAcceptFailure_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 9, 4),
    _XfSwAcceptFailure_Type()
)
xfSwAcceptFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwAcceptFailure.setStatus("current")
_XfSwLmUpgradeTable_Object = MibTable
xfSwLmUpgradeTable = _XfSwLmUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10)
)
if mibBuilder.loadTexts:
    xfSwLmUpgradeTable.setStatus("current")
_XfSwLmUpgradeEntry_Object = MibTableRow
xfSwLmUpgradeEntry = _XfSwLmUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1)
)
xfSwLmUpgradeEntry.setIndexNames(
    (0, "XF-SOFTWARE-MIB", "xfSwLmUpgradeIndex"),
)
if mibBuilder.loadTexts:
    xfSwLmUpgradeEntry.setStatus("current")


class _XfSwLmUpgradeIndex_Type(Integer32):
    """Custom type xfSwLmUpgradeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_XfSwLmUpgradeIndex_Type.__name__ = "Integer32"
_XfSwLmUpgradeIndex_Object = MibTableColumn
xfSwLmUpgradeIndex = _XfSwLmUpgradeIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 1),
    _XfSwLmUpgradeIndex_Type()
)
xfSwLmUpgradeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLmUpgradeIndex.setStatus("current")
_XfSwLmUpgradeProductNumber_Type = XfProductnumber
_XfSwLmUpgradeProductNumber_Object = MibTableColumn
xfSwLmUpgradeProductNumber = _XfSwLmUpgradeProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 3),
    _XfSwLmUpgradeProductNumber_Type()
)
xfSwLmUpgradeProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLmUpgradeProductNumber.setStatus("current")
_XfSwLmUpgradeRevision_Type = XfProductRevision
_XfSwLmUpgradeRevision_Object = MibTableColumn
xfSwLmUpgradeRevision = _XfSwLmUpgradeRevision_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 4),
    _XfSwLmUpgradeRevision_Type()
)
xfSwLmUpgradeRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwLmUpgradeRevision.setStatus("current")


class _XfSwLmUpgradeAdminStatus_Type(Integer32):
    """Custom type xfSwLmUpgradeAdminStatus based on Integer32"""
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
        *(("upgradeStarted", 1),
          ("upgradeAborted", 2),
          ("activeAndRunning", 3),
          ("upgradeTest", 4))
    )


_XfSwLmUpgradeAdminStatus_Type.__name__ = "Integer32"
_XfSwLmUpgradeAdminStatus_Object = MibTableColumn
xfSwLmUpgradeAdminStatus = _XfSwLmUpgradeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 6),
    _XfSwLmUpgradeAdminStatus_Type()
)
xfSwLmUpgradeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSwLmUpgradeAdminStatus.setStatus("current")


class _XfSwLmUpgradeOperStatus_Type(Integer32):
    """Custom type xfSwLmUpgradeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              421,
              425,
              426,
              450,
              451,
              452,
              501,
              502,
              503,
              504,
              530,
              532,
              550,
              552,
              553)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("upgradeStarted", 2),
          ("upgradeFinished", 3),
          ("upgradeTested", 4),
          ("upgradeFailed", 5),
          ("upgradeAborted", 6),
          ("errorInternalError", 50),
          ("errorFileStorage", 51),
          ("ftpPingFailed", 52),
          ("ftpNoAccess", 53),
          ("ftpConnectionDetailsMissing", 54),
          ("ftpConnectionDetailsInvalid", 55),
          ("ftpConnectionTimeout", 56),
          ("ftpNoSuchRemoteFile", 57),
          ("ftpNoSuchRemoteDir", 58),
          ("ftpServiceNotAvailable", 421),
          ("ftpUnableToOpenDataConnection", 425),
          ("ftpConnectionClosed", 426),
          ("ftpFileBusy", 450),
          ("ftpLocalError", 451),
          ("ftpInsufficienStorageSpace", 452),
          ("ftpSyntaxError", 501),
          ("ftpCommandNotImplemented", 502),
          ("ftpBadSequenceCommands", 503),
          ("ftpParameterNotImplemented", 504),
          ("ftpNotLoggedIn", 530),
          ("ftpNeedAccount", 532),
          ("ftpFileUnavailable", 550),
          ("ftpExceededStorageAllocation", 552),
          ("ftpFileNameNotAllowed", 553))
    )


_XfSwLmUpgradeOperStatus_Type.__name__ = "Integer32"
_XfSwLmUpgradeOperStatus_Object = MibTableColumn
xfSwLmUpgradeOperStatus = _XfSwLmUpgradeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 7),
    _XfSwLmUpgradeOperStatus_Type()
)
xfSwLmUpgradeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLmUpgradeOperStatus.setStatus("current")


class _XfSwLmUpgradeProgress_Type(Integer32):
    """Custom type xfSwLmUpgradeProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XfSwLmUpgradeProgress_Type.__name__ = "Integer32"
_XfSwLmUpgradeProgress_Object = MibTableColumn
xfSwLmUpgradeProgress = _XfSwLmUpgradeProgress_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 8),
    _XfSwLmUpgradeProgress_Type()
)
xfSwLmUpgradeProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLmUpgradeProgress.setStatus("current")
if mibBuilder.loadTexts:
    xfSwLmUpgradeProgress.setUnits("percent")


class _XfSwLmUpgradeFailure_Type(Integer32):
    """Custom type xfSwLmUpgradeFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloadFailure", 1),
          ("programFailure", 2),
          ("noFailure", 3))
    )


_XfSwLmUpgradeFailure_Type.__name__ = "Integer32"
_XfSwLmUpgradeFailure_Object = MibTableColumn
xfSwLmUpgradeFailure = _XfSwLmUpgradeFailure_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 9),
    _XfSwLmUpgradeFailure_Type()
)
xfSwLmUpgradeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLmUpgradeFailure.setStatus("current")


class _XfSwLmUpgradeDescription_Type(SnmpAdminString):
    """Custom type xfSwLmUpgradeDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_XfSwLmUpgradeDescription_Type.__name__ = "SnmpAdminString"
_XfSwLmUpgradeDescription_Object = MibTableColumn
xfSwLmUpgradeDescription = _XfSwLmUpgradeDescription_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 10, 1, 10),
    _XfSwLmUpgradeDescription_Type()
)
xfSwLmUpgradeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwLmUpgradeDescription.setStatus("current")


class _XfSwGlobalState_Type(Bits):
    """Custom type xfSwGlobalState based on Bits"""
    namedValues = NamedValues(
        *(("noUpgrade", 0),
          ("sblStarted", 1),
          ("sblWaitForActivate", 2),
          ("sblWaitForCommit", 3),
          ("manualStarted", 4),
          ("manualWaitForActivate", 5),
          ("manualWaitForCommit", 6),
          ("unitUpgrade", 7),
          ("cachingLoadModules", 8),
          ("preparingForTest", 9))
    )

_XfSwGlobalState_Type.__name__ = "Bits"
_XfSwGlobalState_Object = MibScalar
xfSwGlobalState = _XfSwGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 1, 11),
    _XfSwGlobalState_Type()
)
xfSwGlobalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSwGlobalState.setStatus("current")
_XfSwConformance_ObjectIdentity = ObjectIdentity
xfSwConformance = _XfSwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2)
)
_XfSwCompliances_ObjectIdentity = ObjectIdentity
xfSwCompliances = _XfSwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 1)
)
_XfSwGroups_ObjectIdentity = ObjectIdentity
xfSwGroups = _XfSwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2)
)

# Managed Objects groups

xfSwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2, 1)
)
xfSwGroup.setObjects(
      *(("XF-SOFTWARE-MIB", "xfSwRelease"),
        ("XF-SOFTWARE-MIB", "xfSwLoadModuleIndex"),
        ("XF-SOFTWARE-MIB", "xfSwLoadModuleProductNumber"),
        ("XF-SOFTWARE-MIB", "xfSwLoadModuleRevision"),
        ("XF-SOFTWARE-MIB", "xfSwLoadModuleOperStatus"),
        ("XF-SOFTWARE-MIB", "xfSwReleaseIndex"),
        ("XF-SOFTWARE-MIB", "xfSwReleaseProductNumber"),
        ("XF-SOFTWARE-MIB", "xfSwReleaseRevision"),
        ("XF-SOFTWARE-MIB", "xfSwReleaseAdminStatus"),
        ("XF-SOFTWARE-MIB", "xfSwReleaseOperStatus"),
        ("XF-SOFTWARE-MIB", "xfSwActiveRelease"),
        ("XF-SOFTWARE-MIB", "xfSwBootTime"),
        ("XF-SOFTWARE-MIB", "xfSwCommitType"),
        ("XF-SOFTWARE-MIB", "xfSwBoardProductNumber"),
        ("XF-SOFTWARE-MIB", "xfSwBoardRevision"),
        ("XF-SOFTWARE-MIB", "xfSwNpuPassiveProductNumber"),
        ("XF-SOFTWARE-MIB", "xfSwNpuPassiveSwitch"),
        ("XF-SOFTWARE-MIB", "xfSwLoadModuleFailure"),
        ("XF-SOFTWARE-MIB", "xfSwNpuPassiveRevision"),
        ("XF-SOFTWARE-MIB", "xfSwBoardStatus"))
)
if mibBuilder.loadTexts:
    xfSwGroup.setStatus("current")

xSwGroupR2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2, 2)
)
xSwGroupR2.setObjects(
      *(("XF-SOFTWARE-MIB", "xfSwBoardSuProgress"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeIndex"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeProductNumber"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeRevision"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeAdminStatus"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeOperStatus"),
        ("XF-SOFTWARE-MIB", "xfSwBoardMinProductNumber"),
        ("XF-SOFTWARE-MIB", "xfSwBoardMinRevision"),
        ("XF-SOFTWARE-MIB", "xfSwVersionControl"),
        ("XF-SOFTWARE-MIB", "xfSwLoadModuleProgress"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeFailure"),
        ("XF-SOFTWARE-MIB", "xfSwBoardTrafficDisturbance"),
        ("XF-SOFTWARE-MIB", "xfSwReleaseSBLType"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeProgress"),
        ("XF-SOFTWARE-MIB", "xfSwAutoUpgrade"),
        ("XF-SOFTWARE-MIB", "xfSwAutoDowngrade"),
        ("XF-SOFTWARE-MIB", "xfSwGlobalState"),
        ("XF-SOFTWARE-MIB", "xfSwAcceptFailure"),
        ("XF-SOFTWARE-MIB", "xfSwLoadModuleDescription"),
        ("XF-SOFTWARE-MIB", "xfSwLmUpgradeDescription"))
)
if mibBuilder.loadTexts:
    xSwGroupR2.setStatus("current")

xfSwObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 2, 3)
)
xfSwObsoleteGroup.setObjects(
      *(("XF-SOFTWARE-MIB", "xfSwBoardLoadModuleIndex"),
        ("XF-SOFTWARE-MIB", "xfSwBoardLoadModuleType"))
)
if mibBuilder.loadTexts:
    xfSwObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xfSwFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 81, 2, 7, 2, 1, 1)
)
xfSwFullCompliance.setObjects(
      *(("XF-SOFTWARE-MIB", "xfSwGroup"),
        ("XF-SOFTWARE-MIB", "xSwGroupR2"))
)
if mibBuilder.loadTexts:
    xfSwFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XF-SOFTWARE-MIB",
    **{"XfSwRelease": XfSwRelease,
       "XfSwEnableDisable": XfSwEnableDisable,
       "xfSoftwareMIB": xfSoftwareMIB,
       "xfSwObjects": xfSwObjects,
       "xfSwLoadModuleTable": xfSwLoadModuleTable,
       "xfSwLoadModuleEntry": xfSwLoadModuleEntry,
       "xfSwRelease": xfSwRelease,
       "xfSwLoadModuleIndex": xfSwLoadModuleIndex,
       "xfSwLoadModuleProductNumber": xfSwLoadModuleProductNumber,
       "xfSwLoadModuleRevision": xfSwLoadModuleRevision,
       "xfSwLoadModuleOperStatus": xfSwLoadModuleOperStatus,
       "xfSwLoadModuleFailure": xfSwLoadModuleFailure,
       "xfSwLoadModuleProgress": xfSwLoadModuleProgress,
       "xfSwLoadModuleDescription": xfSwLoadModuleDescription,
       "xfSwReleaseTable": xfSwReleaseTable,
       "xfSwReleaseEntry": xfSwReleaseEntry,
       "xfSwReleaseIndex": xfSwReleaseIndex,
       "xfSwReleaseProductNumber": xfSwReleaseProductNumber,
       "xfSwReleaseRevision": xfSwReleaseRevision,
       "xfSwReleaseAdminStatus": xfSwReleaseAdminStatus,
       "xfSwReleaseOperStatus": xfSwReleaseOperStatus,
       "xfSwReleaseSBLType": xfSwReleaseSBLType,
       "xfSwActiveRelease": xfSwActiveRelease,
       "xfSwBootTime": xfSwBootTime,
       "xfSwCommitType": xfSwCommitType,
       "xfSwBoardTable": xfSwBoardTable,
       "xfSwBoardEntry": xfSwBoardEntry,
       "xfSwBoardLoadModuleIndex": xfSwBoardLoadModuleIndex,
       "xfSwBoardLoadModuleType": xfSwBoardLoadModuleType,
       "xfSwBoardProductNumber": xfSwBoardProductNumber,
       "xfSwBoardRevision": xfSwBoardRevision,
       "xfSwBoardStatus": xfSwBoardStatus,
       "xfSwBoardSuProgress": xfSwBoardSuProgress,
       "xfSwBoardMinProductNumber": xfSwBoardMinProductNumber,
       "xfSwBoardMinRevision": xfSwBoardMinRevision,
       "xfSwBoardTrafficDisturbance": xfSwBoardTrafficDisturbance,
       "xfSwNpuObjects": xfSwNpuObjects,
       "xfSwNpuPassiveProductNumber": xfSwNpuPassiveProductNumber,
       "xfSwNpuPassiveRevision": xfSwNpuPassiveRevision,
       "xfSwNpuPassiveSwitch": xfSwNpuPassiveSwitch,
       "xfSwLoadModuleTypes": xfSwLoadModuleTypes,
       "xfDeviceProcessorSoftware": xfDeviceProcessorSoftware,
       "xfPciFpgaCode": xfPciFpgaCode,
       "xfSwUpgradePreferences": xfSwUpgradePreferences,
       "xfSwVersionControl": xfSwVersionControl,
       "xfSwAutoUpgrade": xfSwAutoUpgrade,
       "xfSwAutoDowngrade": xfSwAutoDowngrade,
       "xfSwAcceptFailure": xfSwAcceptFailure,
       "xfSwLmUpgradeTable": xfSwLmUpgradeTable,
       "xfSwLmUpgradeEntry": xfSwLmUpgradeEntry,
       "xfSwLmUpgradeIndex": xfSwLmUpgradeIndex,
       "xfSwLmUpgradeProductNumber": xfSwLmUpgradeProductNumber,
       "xfSwLmUpgradeRevision": xfSwLmUpgradeRevision,
       "xfSwLmUpgradeAdminStatus": xfSwLmUpgradeAdminStatus,
       "xfSwLmUpgradeOperStatus": xfSwLmUpgradeOperStatus,
       "xfSwLmUpgradeProgress": xfSwLmUpgradeProgress,
       "xfSwLmUpgradeFailure": xfSwLmUpgradeFailure,
       "xfSwLmUpgradeDescription": xfSwLmUpgradeDescription,
       "xfSwGlobalState": xfSwGlobalState,
       "xfSwConformance": xfSwConformance,
       "xfSwCompliances": xfSwCompliances,
       "xfSwFullCompliance": xfSwFullCompliance,
       "xfSwGroups": xfSwGroups,
       "xfSwGroup": xfSwGroup,
       "xSwGroupR2": xSwGroupR2,
       "xfSwObsoleteGroup": xfSwObsoleteGroup}
)
